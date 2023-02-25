from rest_framework import serializers
from measurement.models import Sensor, Measurement

# TODO: опишите необходимые сериализаторы
class MeasurementSerializers(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['temperature', 'date']


class SensorSerializersLow(serializers.ModelSerializer):
    measurements = MeasurementSerializers(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'title', 'description']


class SensorSerializersHigh(serializers.ModelSerializer):
    measurements = MeasurementSerializers(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'title', 'description', 'measurements']