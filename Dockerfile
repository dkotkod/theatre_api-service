FROM python:3.11.9-alpine3.20
LABEL maintainer = "dkotkod@gmail.com"

WORKDIR app/

ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .
