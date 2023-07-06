FROM python:3.7.11-slim-stretch
ENV PYTHONUNBUFFERED 1
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

ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5000

ADD . .

ENTRYPOINT [ "gunicorn", "app:app", "-b", "localhost:5000 &" ]

CMD ["flask", "run"]