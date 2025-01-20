FROM python:3.13.1-slim-bullseye

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update &&\ 
    apt-get install --assume-yes --no-install-recommends -y\
    build-essential

RUN pip3 install --no-cache-dir --upgrade pip
RUN pip3 install --no-cache-dir wheel poetry