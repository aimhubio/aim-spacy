from typing import Dict, Any, Tuple, Union, Callable, List, Optional, IO
import sys
from weakref import finalize

from spacy import Language, displacy
from spacy.training.loggers import console_logger

from aim_spacy import AimDisplaCy
from aim_spacy.handler import Handler
from aim_spacy.utils import docbin_to_doc

try:
    import aim
    # test that these are available
    from aim import Run, Repo,Image,Text  # noqa: F401
except ImportError:
    raise ImportError(
        'We cannot find the "aim" package on your system. Please make sure to install it.'
    )

# entry point: spacy.AimLogger.v1
def aim_logger_v1(
    repo: Optional[str] = '.',
    experiment_name: Optional[str] = None,
    run_hash: Optional[str] = None,
    viz_path: Optional[str] = None,
    model_log_interval: Optional[int] = None,
    image_size: Optional[str] = "600,200",
    experiment_type: Optional[str] = None,
    options: Optional[dict] = {},

):
    
    console = console_logger(progress_bar=False)

    # aim_run, console_log_step, console_finalize = setup_aim(experiment_name=experiment_name)
    def setup_aim(nlp: 'Language', stdout: IO = sys.stdout, stderr: IO = sys.stderr, experiment_name:str=experiment_name) \
        -> Union[Run, Callable[[Dict[str, Any]], None], Callable[[], None]]:

            nonlocal viz_path, model_log_interval, image_size, experiment_type, options

            config = nlp.config.interpolate()

            aim_run = Run(repo = repo, experiment=experiment_name, run_hash=run_hash)
            aim_run['config'] = config

            if viz_path is not None:
                image_size = tuple([int(size.strip()) for size in image_size.split(',')])
                aim_displacy = AimDisplaCy(image_size=image_size, **options)

                logging_handler = Handler()
                logging_handler.data = docbin_to_doc(docbin_path=viz_path, nlp=nlp)

            console = console_logger(progress_bar=False)
            console_log_step, console_finalize = console(nlp, stdout, stderr)

            def aim_log_step(info: Optional[Dict[str, Any]]):

                logging_handler = Handler()

                console_log_step(info)

                if info is not None:
                    epoch = info['epoch']
                    step = info['step']

                    score = info['score']
                    other_scores = info['other_scores']
                    losses = info['losses']
                    aim_run.track(score , name = 'Score', context = {'type':'score'})
                    if losses:
                        for loss_name, loss_value in losses.items():
                            aim_run.track(loss_value, name=loss_name, context={'type':f'loss_{loss_name}'}, epoch=epoch, step=step)

                    if isinstance(other_scores, dict):
                        for score_name, loss_value in other_scores.items():
                            if not isinstance(loss_value, dict):
                                aim_run.track(loss_value, name=loss_name, context={'type':f'other_scores_{score_name}'}, epoch=epoch, step=step)

                    if model_log_interval is not None:
                        if (info["step"] % model_log_interval == 0 and info["step"] != 0):

                            displacy_input = dict(docs=logging_handler.data, style=experiment_type, caption=f'Visualization at step: {info["step"]}')                   
                            aim_run.track(aim_displacy(**displacy_input), step=step, epoch=epoch, name='Parsing', context={'type': experiment_type})                           


            def aim_finalize():
                nonlocal aim_run
                console_finalize()
                aim_run.close()
                aim_run = None


            return aim_log_step, aim_finalize


    return setup_aim
