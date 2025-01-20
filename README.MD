# Goal: crear un projecte from scratch

## Step 1

- Crear workspace: doc <https://code.visualstudio.com/docs/editor/workspaces>
- Crear la carpeta del .devcontainer
- Crear el .devcontainer.json <https://code.visualstudio.com/docs/devcontainers/create-dev-container>
- Un Dockerfile que faci un Docker pull de Python 3.13
image-repo <https://hub.docker.com/_/python/>
image-names <https://medium.com/@faruk13/alpine-slim-bullseye-bookworm-noble-differences-in-docker-images-explained-d9aa6efa23ec>

Al Dockerfile hi ha d'haver:

- apt update
- apt install build-essentials
- Instal.lar poetry i pip

- Crear un fitxer poetry from scratch <https://python-poetry.org/>
- Mirar la documentació oficial de poetry
- Afegir-hi els els següents paquets: pandas, scikit-learn
- Afegir-hi els següents paquets de desenvolupament: ruff
- Implementar algun exemple de scikit de ML que faci servir moltes dates i que trigui molt a entrenar

### Entry point

Dos scripts: fit i predict. Tot dins d'un entry point: demo
- demo train
- demo predict

````
[tool.poetry.scripts]
demo="demo.__main__:_main"
````

You will need to execute the following commands

```
poetry run demo train
poetry run demo predict
```

To be able to execute the commands without typing "poetry run" you must access the virtual environment created by poetry. You can get the env path entering the following command:

````
poetry env activate
````

Once in the poetry environment you can use the entry points. An to get out of the environment just type the following command.
````
deactivate
````

## Step 2

- Farem un segon Dockerfile dins fora de la carpeta de .devcontainer
- Semblant al del .devcontainer
- En aquest sí que farem un poetry install de tots els paquets
- Docker build d'aquest Dockerfile
````
    docker build -f Dockerfile -t demoimage .
````
- Crear container i executar exemple
````
    docker run -it --rm demoimage bash
    docker run -it --rm demoimage demo train
    docker run -it --rm demoimage demo predict
````

## Step 3

- Executar el codi dins del container però estressant el container