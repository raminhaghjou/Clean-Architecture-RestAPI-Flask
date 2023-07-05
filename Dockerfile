FROM python:3.7.11-slim-stretch
LABEL authors="ramin"
ARG USER_NAME=aiapp
ARG USER_HOME=/home/${USER_NAME}

RUN useradd -ms /bin/bash -d ${USER_HOME} ${USER_NAME} \
    && apt update \
    && apt upgrade -y \
    && apt install nginx supervisor -y \
    && pip install --no-cache pipenv \
    && apt-cache clean

WORKDIR ${USER_HOME}

ADD ./Pipfile ./Pipfile
RUN pipenv lock --pre && pipenv sync

ADD ./app ./app

EXPOSE 5000

ENTRYPOINT [ "gunicorn", "app:app", "-b", "localhost:5000 &" ]