from tqdm import tqdm
import argparse

import spacy
import aim
from aim_spacy import AimDisplaCy


def load_data(data_path=''):
    data = []
    with open(args.data_path) as f:
        for line in f.readlines():
            data.append(line.strip())
    return data


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Aim-Spacy integration Namespace"
    )

    parser.add_argument('--data_path', help='Path to textualt data file')

    parser.add_argument(
        '--remote_tracking_server',
        default=None,
        help="The name of the experiment to assign"
    )

    parser.add_argument(
        '--model_name',
        help="The name of the model to use"
    )

    parser.add_argument(
        '--experiment_name',
        help="The name of the experiment to assign"
    )

    args = parser.parse_args()

    experiment_name = args.experiment_name
    if args.remote_tracking_server is not None:
        remote_tracking_server = f'aim://{args.remote_tracking_server}'
        aim_run = aim.Run(experiment=experiment_name, repo=remote_tracking_server)
    else:
        aim_run = aim.Run(experiment=experiment_name)

    nlp = spacy.load(args.model_name)
    data = load_data(args.data_path)

    for index, text in tqdm(enumerate(data), total=len(data)):
        doc = nlp(text)
        
        if len(doc.ents) > 0:
            aim_run.track(
                AimDisplaCy(doc, style='dep', caption=f'Dependecy for data: {index}'),
                name='Parsing',
                context={'type': 'dependency'}
            )

            aim_run.track(
                AimDisplaCy(doc, style='ent', caption=f'Entity for data: {index}'),
                name='Parsing',
                context={'type': 'entity'}
            )
