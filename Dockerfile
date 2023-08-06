FROM python:alpine

COPY ./smart_home/requirements.txt /src/requirements.txt

RUN pip3 install -r /src/requirements.txt

COPY . /src

WORKDIR src

RUN python ./smart_home/manage.py migrate

EXPOSE 8880
#
##
CMD ["python", "./smart_home/manage.py", "runserver", "0.0.0.0:8880"]


