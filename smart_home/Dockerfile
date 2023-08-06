FROM python:3.8

#COPY ./requirements.txt /src/requirements.txt
WORKDIR /app


RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

RUN chmod +x ./entrypoint.sh
#
#WORKDIR src
#RUN python ./smart_home/manage.py migrate

EXPOSE 8000

ENTRYPOINT ["./entrypoint.sh"]
#
##
#CMD ["python", "./smart_home/manage.py", "runserver", "0.0.0.0:8880"]


