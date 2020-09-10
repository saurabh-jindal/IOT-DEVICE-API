from rest_framework import serializers
from . import models


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Device
        fields = '__all__'
    

class HumiditySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HumidReading
        fields = '__all__'
    

class TempSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TempReading
        fields = '__all__'
    
