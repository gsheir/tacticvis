# TacticVis

This repo uses free data from [Hudl StatsBomb](https://statsbomb.com/).

Full match replays, where used, are credited below:
- [UEFA Women's Euro 2022: Final](https://www.uefa.tv/video/vod/379782/?bucketExId=pnAe&lastSeen=0%3A379782&section=WEURO)

For detailed descriptions of the purpose and design of the product, see our [wiki](https://github.com/gsheir/football_analysis/wiki/TacticVis-Wiki-%E2%80%90-Home).

## Environment setup

You may use one of the following methods:

### Using VSCode Dev Containers (recommended)

This repo uses [Dev Containers](https://code.visualstudio.com/docs/devcontainers/containers). Please follow the instructions above to install the extension.

To set up your environment, use the Command Palette (Ctrl+Shift+P) in VSCode and select "Dev Containers: Reopen in Container". This will open a new VSCode window and install the neccesary prerequisites.

![Screenshot of reopen in container](https://code.visualstudio.com/assets/docs/devcontainers/create-dev-container/dev-containers-reopen.png)


### Creating your dev environment manually

#### Installing Docker and PostgreSQL

- Docker: [installation instructions](https://docs.docker.com/desktop/)
- PostgreSQL: We deploy the database in a Docker image but you may want to install the PSQL CLI or other tools: [installation instructions](https://www.postgresql.org/download/) 

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

#### Starting the database
Navigate to `./.devcontainer` and run 
```
docker compose up -d
```

which will start the database. 

## Running the application



To run the web app, navigate to `./web_app/tacticvis` and run

```
python manage.py runserver
```

The application is now available on `localhost:8000`