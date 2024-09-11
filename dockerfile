FROM python:3.9.18-slim-bullseye

LABEL Version="1.0"
LABEL Author="Anagh Patel"
LABEL MAINTAINER="anaghpatel28@gmail.com"

USER root
RUN mkdir -p /LibRizz

COPY . /LibRizz

WORKDIR /LibRizz

RUN python3 -m pip install -r requirements.txt

CMD [ "python3","headless.py"]
