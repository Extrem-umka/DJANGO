from django.urls import path

from django.conf.urls import include
from django.contrib import admin

from rest_framework.routers import DefaultRouter
from measurement.views import SensorViewSet, MeasurementViewSet


router = DefaultRouter()
router.register('sensors', SensorViewSet)
router.register('measurements', MeasurementViewSet, basename='measurements')

urlpatterns = router.urls