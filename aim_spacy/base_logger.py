from typing import Dict, Any, Tuple, Union, Callable, List, Optional, IO
import sys
from weakref import finalize

from spacy import util
from spacy import Language
from spacy.training.loggers import console_logger

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

):
    
    console = console_logger(progress_bar=False)
    # aim_run, console_log_step, console_finalize = setup_aim(experiment_name=experiment_name)
    def setup_aim(nlp: 'Language', stdout: IO = sys.stdout, stderr: IO = sys.stderr, experiment_name:str='') \
        -> Union[Run, Callable[[Dict[str, Any]], None], Callable[[], None]]:
            config = nlp.config.interpolate()

            aim_run = Run(repo = repo, experiment=experiment_name, run_hash=run_hash)
            aim_run['config'] = config

            console = console_logger(progress_bar=False)
            console_log_step, console_finalize = console(nlp, stdout, stderr)

            def aim_log_step(info: Optional[Dict[str, Any]]):
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


            def aim_finalize():
                nonlocal aim_run
                console_finalize()
                aim_run.close()
                aim_run = None


            return aim_log_step, aim_finalize


    return setup_aim
