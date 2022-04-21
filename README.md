# Aim-spaCy

The project contains the fundamental integration in between `Aim` and `spaCy`.

[badges] and [links]

[demo screenshot]

## About

Aim-spaCy helps to easily collect, store and explore training logs of spaCy, including:
- metrics
- hyper-parameters
- displaCy visualizations

Find more about Aim at https://github.com/aimhubio/aim

spacy: https://github.com/explosion/spaCy

## Examples

- A quick example on how to tracking metrics, hparams and displacy outputs with AimLogger
  - https://github.com/aimhubio/aim-spacy/tree/master/examples/training_demo 
- Exampl of tracking displacy visualizations with AimDisplaCy
  - https://github.com/aimhubio/aim-spacy/tree/master/examples/image_tracking_demo

## Getting Started

### 1. Installation

Install Aim-spaCy by running:
```
pip install aim-spacy
```

### 2. Tracking metrics, hparams and displacy visualizations

<details>
  <summary>1. Tracking with AimLogger</summary>
  
`spacy.AimLogger.v1` allows the user to leverage [`Aim`](https://aimstack.io/) as the experiment tracker throughout the model development cycles. All of the training metrics will be tracked by the `Aim` through the training steps and can be easily accessed through Aim UI.


It is important to note that you can observe the changes in the metrics live throughout the training. Aim also supports tracking multiple experiments simultaneously. Aim will store all of the [training config](https://spacy.io/usage/training#config) hyperparameters that are used during experimentation along with [system-related information](https://aimstack.readthedocs.io/en/latest/ui/pages/run_management.html#id7) ranging from GPU/CPU usability to Disk IO. This comes in with an added benefit that you can search/filter across the experimentation rather granularly, using our pythonic search [AimQL](https://aimstack.readthedocs.io/en/latest/using/search.html?highlight=AimQL#searching), live from the UI. To access the Aim Logger one can simply add a config akin to this


Example config:

```ini
[training.logger]
@loggers = "spacy.AimLogger.v1"
repo = "path/to/save/logs"
experiment_name = "your_experiment_name"
```

The complete overview of Aim Logger inputs looks like this.

| Name                   | Type | Description|
| ---------------------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `repo`         | `str`           | The path for saving the logs        |
| `experiment_name` | `str`     | The name of the experiment to track(default: `None`, the experiment will be determined by hash).                                                                                                                                       |
| `viz_path`   | `str` | The path of the dataset (in a .spacy format) that will be used for saving the visualisations during training. Usually, this is taken as the dev set (dev.spacy) For a standalone run, this option is not needed (default: `None`).               |
| `model_log_interval`   | `int` |How often should the model log the experimentation results               |
| `image_size`   | `str` | A string with a ',' separation designating the height and width of the image that is going to be saved during the training              |
| `experiment_type`   | `str` | This flag designates what kind of an experiment is currently being tracked. If 'ner' or 'dep' is specified then the tracker will also use the `viz_path` and `image_size` for tracking displacy outputs during training. For a standalone run, this option is not needed (default: `None`).               ||

</details>

<details>
  <summary>2. Tracking in any python script</summary>

Track metrics and hparams
```py
from aim import Run

run = Run()

# Save inputs, hparams or any other `key: value` pairs
run['hparams'] = {
    'learning_rate': 0.001,
    'batch_size': 32,
}

# ...
for step in range(10):
    # Log metrics to visualize performance
    run.track(step, name='metric_name')
# ...
```

Track displacy visulizations
```py
from aim_displacy import AimDisplaCy
from aim import Run

aim_run = Run()

aim_displacy = AimDisplaCy(image_size=(600, 200))

for index, text in tqdm(enumerate(data), total=len(data)):
    doc = nlp(text)
    aim_run.track(
        aim_displacy(doc, style='dep', caption=f'Dependecy for data: {index}'),
        name='Parsing',
        context={'type': 'dependency'}
    )
    aim_run.track(
        aim_displacy(doc, style='ent', caption=f'Entity for data: {index}'),
        name='Parsing',
        context={'type': 'entity'}
    )
```
  
</details>

### 3. Browsing results with Aim UI

Execute the below command to run Aim UI:
```shell
aim up
```

You should see the following output meaning Aim UI is up and running:
```
Running Aim UI on repo `<Repo#-5930451821203570655 path=/.aim read_only=None>`
Open http://127.0.0.1:43800
Press Ctrl+C to exit
```

Open your browser and navigate to http://127.0.0.1:43800 

You should be able to see the home page of Aim UI!
