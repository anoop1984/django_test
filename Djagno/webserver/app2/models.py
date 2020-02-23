from django.db import models

# Create your models here.

#class <nameoftable>

class service(models.Model):
      name = models.CharField(max_length=20)
      description = models.CharField(max_length=100)
      service_id = models.IntegerField() 
      status= models.BooleanField()
