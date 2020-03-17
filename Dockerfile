FROM python:3.8-alpine3.11
ENV PYTHONUNBUFFERED 1

RUN echo "http://dl-3.alpinelinux.org/alpine/edge/main/" >>/etc/apk/repositories
RUN echo "http://dl-3.alpinelinux.org/alpine/edge/community/" >>/etc/apk/repositories

RUN apk update \
    && apk add gdal-dev geos-dev \
    && apk add postgresql-dev gcc python3-dev musl-dev

RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/