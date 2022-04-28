<div align="center">
  
<br />

<img src="https://user-images.githubusercontent.com/13848158/136364717-0939222c-55b6-44f0-ad32-d9ab749546e4.png" height="70" />

<br />
<br />

[![PyPI Package](https://img.shields.io/pypi/v/aim?color=yellow)](https://pypi.org/project/aim-spacy/)
[![PyPI Downloads](https://img.shields.io/pypi/dw/aim?color=green)](https://pypi.org/project/aim-spacy/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/aim)](https://pypi.org/project/aim-spacy/)
[![Issues](https://img.shields.io/github/issues/aimhubio/aim)](http://github.com/aimhubio/aim-spacy/issues)
[![License](https://img.shields.io/badge/License-Apache%202.0-orange.svg)](https://opensource.org/licenses/Apache-2.0)

# Aim-spaCy integration

The project contains the fundamental integration in between `Aim` and `spaCy`.

## AimLogger

In order to use aim for experimentation tracking, you must install it onto your system.

```
pip install aim-spacy
```

### Usage

`spacy.AimLogger.v1` allows the user to leverage [`Aim`](https://aimstack.io/) as the experiment tracker throughout the model development cycles. All of the training metrics will be tracked by the `Aim` through the training steps and can be easily accessed through Aim UI by simply running 

```
aim up
```

There are several options to change the starting options using [Aim](https://aimstack.readthedocs.io/en/latest/refs/cli.html#up).

It is important to note that you can observe the changes in the metrics live throughout the training. Aim also supports tracking multiple experiments simultaneously. Aim will store all of the [training config](https://spacy.io/usage/training#config) hyperparameters that are used during experimentation along with [system-related information](https://aimstack.readthedocs.io/en/latest/ui/pages/run_management.html#id7) ranging from GPU/CPU usability to Disk IO. This comes in with an added benefit that you can search/filter across the experimentation rather granularly, using our pythonic search [AimQL](https://aimstack.readthedocs.io/en/latest/using/search.html?highlight=AimQL#searching), live from the UI. To access the Aim Logger one can simply add a config akin to this


### Example config

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


Using the full scale of `aim-spacy` integration it is possible to aggregate/group and filter your experiments with various levels of granularity

<!-- ![](https://user-images.githubusercontent.com/8036160/165744936-424c96ce-fed2-4453-b903-7356dea0be0f.svg) -->

![grouped_img](https://user-images.githubusercontent.com/8036160/165745270-231f6db5-6c43-4647-b226-30b22b8030f1.png)

You can also filter using all the  parametrs  with `Aim`s pythonic search engine `AimQL`

![aimQL-img](https://uploads-ssl.webflow.com/62558278c40852a7dfff6c09/62558278c408525151ff6c5e_2.png)

Tracking NER's and dependecies during training is also integrated within the pipeline

![ner_dep_img](https://uploads-ssl.webflow.com/623c6d08838e92013e0cc115/62596a317852acb967cbc2d2_2.png)


Grouping images along various axis is also entirely possible

![ner_img](https://uploads-ssl.webflow.com/623c6d08838e92013e0cc115/62596a506525a64a2e7e7eae_4.png)
