# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from measurement.models import Sensor
from measurement.serializers import SensorSerializersLow

from measurement.models import Measurement
from measurement.serializers import SensorSerializersHigh, MeasurementSerializers


class SensorView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializersLow


class SensorView2(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializersHigh


class MeasurementView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializers








