from django.urls import path

from measurement.views import MeasurementView

from measurement.views import SensorView, SensorView2

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorView.as_view()),
    path('sensors/<pk>', SensorView2.as_view()),
    path('measurement/', MeasurementView.as_view())
]
