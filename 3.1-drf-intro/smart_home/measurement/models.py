from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)

class Measurement(models.Model):
    # id = models.AutoField(primary_key=True)
    temperature = models.FloatField()
    created_at = models.DateField(auto_now_add=True)
    sensors = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')