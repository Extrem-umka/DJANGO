# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, MeasurementSerializer

class SensorViewSet(ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    http_method_names = ['get', 'post', 'patch']

class MeasurementViewSet(ModelViewSet):
    qyeryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
    http_method_names = ['get', 'post', 'patch']


