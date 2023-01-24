FROM python:3.8.10

WORKDIR /CoinDashApp

COPY ./requirements.txt /requirements.txt

RUN pip install --upgrade -r /requirements.txt

COPY ./CoinDashApp /CoinDashApp
