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
