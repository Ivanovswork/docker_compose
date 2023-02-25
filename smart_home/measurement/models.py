from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
from django.db.models import CASCADE


class Sensor(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)


class Measurement(models.Model):
    id_sensor = models.ForeignKey(Sensor, related_name='sensor', on_delete=CASCADE)
    temperature = models.FloatField()
    date = models.DateTimeField(auto_now=False, auto_now_add=False)