# Examples

Here we provide a demo for using the Aim experiment tracker along with spacy's training pipeline.

We generated the toy example dataset `train.spacy` (A format used within spacy) for NER training using the following command

```
python train.py
```

The generate configs are taken from the [default Spacy pipleine](https://spacy.io/usage/training). The only difference is that we change the configuration for the logger in the following fashion.

```
[training.logger]
@loggers = "spacy.AimLogger.v1"
repo = "./"
experiment_name = "ner_toy"
viz_path = "train.spacy"
model_log_interval = 1
image_size = "600,200"
experiment_type = "ner"
```

The complete set of options for the logger can be checked in the main README.md of the `aim-spacy` package. To start the training process simply use the default spacy command

```
spacy train config.cfg --output ./output --paths.train ./train.spacy --paths.dev ./train.spacy 

```








