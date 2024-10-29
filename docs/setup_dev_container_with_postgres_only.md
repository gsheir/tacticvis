# Set up Dev Containers with Postgres only

This sets up

- A dev container for development work
- A PostgreSQL database container

Any additional tools are installed locally in the dev container, including

- Airflow

## Instructions

### Set up dev container
This repo uses [Dev Containers](https://code.visualstudio.com/docs/devcontainers/containers). Please follow the instructions above to install the extension.

To set up your environment, use the Command Palette (Ctrl+Shift+P) in VSCode and select "Dev Containers: Reopen in Container". This will open a new VSCode window and install the neccesary prerequisites.

![Screenshot of reopen in container](https://code.visualstudio.com/assets/docs/devcontainers/create-dev-container/dev-containers-reopen.png)

### Install Airflow locally

Run the script

```
bash scripts/install_airflow_locally.sh
```

## Run Airflow

In one terminal window, run

```
airflow webserver --port 8080
```

You can then log in to the Airflow webserver on `localhost:8080` on the host with username `admin` and password `admin`

In a separate terminal window, run

```
airflow scheduler
```