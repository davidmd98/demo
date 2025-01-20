FROM python:3.13.1-slim-bullseye

ENV PATH="/app/.venv/bin:$PATH"

RUN pip3 install --no-cache-dir poetry==1.6.1

WORKDIR /app

COPY pyproject.toml poetry.lock /app/
COPY demo /app/demo
COPY README.MD /app/

RUN mkdir -p /app/assets

RUN poetry config virtualenvs.in-project true
RUN poetry install --without dev