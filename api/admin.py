from django.contrib import admin
from .models import Device, TempReading, HumidReading
# Register your models here.
admin.site.register((Device, TempReading, HumidReading))
