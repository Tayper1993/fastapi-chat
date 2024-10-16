FROM python:3.12-slim
LABEL version="0.1.0" maintainer="Polyakov_KS"
ENV PYTHONUNBUFFERED=0
ENV LANG ru_RU.UTF-8

RUN /usr/local/bin/python -m pip install --upgrade pip && rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/*

WORKDIR /usr/src/app
COPY ./requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /code
COPY . /code

EXPOSE 8000

CMD uvicorn app.main:app