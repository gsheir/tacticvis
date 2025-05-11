# TacticVis

This repo uses free data from [Hudl StatsBomb](https://statsbomb.com/).

[!info] Writeups of the analyses can be found here: [Analysis writeups](docs/analysis/index.md)

Full match replays, where used, are credited below:
- [UEFA Women's Euro 2022: Final](https://www.uefa.tv/video/vod/379782/?bucketExId=pnAe&lastSeen=0%3A379782&section=WEURO)


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
