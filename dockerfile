FROM python:3-alpine
RUN pip install minio configparser  #&& apk update && apk add curl
WORKDIR /opt/
COPY main1.py config.cfg 400kb.log 5mb.log 3mb.log ./
RUN ls
