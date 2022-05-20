  
<br />

# Aim-spaCy

<br />

[![PyPI Package](https://img.shields.io/pypi/v/aim-spacy?color=yellow)](https://pypi.org/project/aim-spacy/)
[![PyPI Downloads](https://img.shields.io/pypi/dw/aim-spacy?color=green)](https://pypi.org/project/aim-spacy/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/aim-spacy)](https://pypi.org/project/aim-spacy/)
[![Issues](https://img.shields.io/github/issues/aimhubio/aim-spacy)](http://github.com/aimhubio/aim-spacy/issues)
[![License](https://img.shields.io/badge/License-Apache%202.0-orange.svg)](https://opensource.org/licenses/Apache-2.0)


[Aim-spaCy](https://aimstack.io/spacy) is an [Aim](https://github.com/aimhubio/aim)-based spaCy experiment tracker. Its mission is to help AI researchers compare their spaCy metadata dramatically faster at scale.

## About
When running spaCy for training and inference a variety of metadata gets generated (hyperparams, metrics, visualizations etc). The runs/inferences need to be compared to do the next iterations quickly.
Aim is the most advanced open-source self-hosted AI experiment / metadata comparison tool.

Aim-spaCy helps to easily collect, store and explore training logs for spaCy, including:
- metrics
- hyper-parameters
- displaCy visualizations

More about Aim: https://github.com/aimhubio/aim

More about spaCy: https://github.com/explosion/spaCy

## Examples

- A quick example on how to track metrics, hparams and displaCy outputs with AimLogger
  - https://github.com/aimhubio/aim-spacy/tree/master/examples/training_demo 
- Example of tracking displaCy visualizations with AimDisplaCy
  - https://github.com/aimhubio/aim-spacy/tree/master/examples/image_tracking_demo



## Getting Started

### 1. Installation

In order to use aim for experimentation tracking, you must install it onto your system.

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

![homescreen_img](https://user-images.githubusercontent.com/8036160/165775219-35fb1e09-e2a9-4f26-a6f4-0cf5273d2ac8.png)

Using the full scale of `aim-spacy` integration it is possible to aggregate/group and filter your experiments with various levels of granularity

<!-- ![](https://user-images.githubusercontent.com/8036160/165744936-424c96ce-fed2-4453-b903-7356dea0be0f.svg) -->

![grouped_img](https://user-images.githubusercontent.com/8036160/165745270-231f6db5-6c43-4647-b226-30b22b8030f1.png)

You can also filter using all the  parametrs  with `Aim`s pythonic search engine `AimQL`

![aimQL-img](https://uploads-ssl.webflow.com/62558278c40852a7dfff6c09/62558278c408525151ff6c5e_2.png)

Tracking NER's and dependecies during training is also integrated within the pipeline

![ner_dep_img](https://uploads-ssl.webflow.com/623c6d08838e92013e0cc115/62596a317852acb967cbc2d2_2.png)


Grouping images along various axis is also entirely possible

![ner_img](https://uploads-ssl.webflow.com/623c6d08838e92013e0cc115/62596a506525a64a2e7e7eae_4.png)
