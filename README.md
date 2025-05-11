# TacticVis

This repo uses free data from [Hudl StatsBomb](https://statsbomb.com/).

> [!TIP] 
> The individual analyses can be found here: [Analysis pieces](docs/analysis/index.md)

Full match replays, where used, are credited in the respective writeups.


## Environment setup

### Creating your dev environment manually

#### Installing Python and packages

We use Python 3.11 and above: [installation instructions](https://www.python.org/downloads/)

This repo uses `pip-compile` to maintain an up-to-date requirements file. In your environment of choice (I use `virtualenv`), download pip-tools:

```
pip install pip-tools
```

and run

```
pip-compile requirements.in
```

to generate the `requirements.txt` file. You can then use 

```
pip install -r requirements.txt
``` 

to install the prerequisites. Do not commit the `requirements.txt` file.
