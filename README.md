# TacticVis

This repo uses free data from [StatsBomb](https://statsbomb.com/).

Full match replays, where used, are credited below:
- [UEFA Women's Euro 2022: Final](https://www.uefa.tv/video/vod/379782/?bucketExId=pnAe&lastSeen=0%3A379782&section=WEURO)

For detailed descriptions of the purpose and design of the product, see our [wiki](https://github.com/gsheir/football_analysis/wiki/TacticVis-Wiki-%E2%80%90-Home).

## Environment setup
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

to install the prerequisites.