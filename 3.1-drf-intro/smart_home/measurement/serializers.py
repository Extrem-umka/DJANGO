from rest_framework import serializers
from measurement.models import Sensor, Measurement
# TODO: опишите необходимые сериализаторы
class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'measurements']


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['id', 'temperature', 'created_at', 'sensors']