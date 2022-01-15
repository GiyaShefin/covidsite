from django.db import models

# Create your models here.
# Create your models here.
from django.db import models

# Create your models here.
class PatientsDetails(models.Model):
    name=models.CharField(max_length=250)
    age=models.IntegerField()
    dob=models.DateField()
    address=models.CharField(max_length=250)
    district=models.CharField(max_length=250)
    firstdose=models.BooleanField()
    seconddose=models.BooleanField()


class City(models.Model):
    name = models.CharField(max_length=128)

class Town(models.Model):
    name = models.CharField(max_length=128)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='towns')
