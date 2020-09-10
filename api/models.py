from django.db import models

# Create your models here.
class Device(models.Model):
    uid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class TempReading(models.Model):
    device = models.ForeignKey(Device, on_delete= models.CASCADE)
    reading = models.CharField(max_length=40)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "New Temp reading added for device " + self.device.name + " is " + self.reading + ' is created on ' + str(self.created_on)
    
class HumidReading(models.Model):
    device = models.ForeignKey(Device, on_delete= models.CASCADE)
    reading = models.CharField(max_length=40)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "New Humidity reading added for device " + self.device.name + " is " + self.reading + ' is created on ' + str(self.created_on)