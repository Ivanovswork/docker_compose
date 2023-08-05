FROM python:3.8

COPY ./smart_home/requirements.txt /src/requirements.txt

WORKDIR src

RUN pip3 install -r requirements.txt
