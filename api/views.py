from django.shortcuts import render
from .serializers import TempSerializer, HumiditySerializer, DeviceSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Device, TempReading, HumidReading
from rest_framework.decorators import api_view
from django.http import Http404
from rest_framework import status
import datetime
# Create your views here.

@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'Create a device' : 'api/devices',
        'Delete a device' : 'api/devices/{device-id}',
        'Get a device' : 'api/devices/{device-id}',
        'List all devices' : 'api/devices',
        'Filter readings' : '/api/devices/{device-uid}/readings/{parameter}/?start_on=yyyy-mm-ddTHH:MM:SS&end_on=yyyy-mm-ddTHH:MM:SS'
    }
    return Response(api_urls)

class Devices(APIView):
    def get(self,request):
        devices = Device.objects.all()
        serializer = DeviceSerializer(devices, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = DeviceSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.error, status = status.HTTP_400_BAD_REQUEST)

class DeviceDetail(APIView):
    def get(self,request,device_id):
        try:
            device = Device.objects.get(pk = device_id)
        except Device.DoesNotExist:
            raise Http404
        serializer = DeviceSerializer(device)
        return Response(serializer.data)
    def delete(self, request, device_id):
        try:
            device = Device.objects.get(pk = device_id)
        except:
            raise Http404
        device.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


class FilterReadings(APIView):
    def get(self, request, device_id, p):
        start_on = request.query_params.get('start_on','')
        end_on = request.query_params.get('end_on','')
        try:
            device = Device.object.get(pk = device_id)[0]
            if(p == 'temperature'):
                reading = TempReading.objects.filter(device = device, created_on__range=(start_on, end_on))
                serializer = TempSerializer(reading)
            else:
                reading = HumidReading.objects.filter(device = device, created_on__range=(start_on, end_on))
                serializer =  HumidSerializer(reading)
        except:
            raise Http404
        return Response(serializer.data)
            
            

            



