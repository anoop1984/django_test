from django.db import models

# Create your models here.

class MonitorLog(models.Model):
     
    testDescription = models.CharField(max_length = 264)
    severity =        models.CharField(max_length = 50)
    ipaddress =       models.CharField(max_length = 50)
    hostname =        models.CharField(max_length = 50) 
    commandExecuter = models.CharField(max_length = 264) 
    verdict =         models.CharField(max_length = 264) 
    remark  =         models.CharField(max_length = 264) 
    testId =          models.CharField(max_length = 100) 
#    timestamp =       models.DateTimeField(auto_now_add=True)
    timestamp =       models.DateTimeField()


#    def __str__(self):
#      return self.MonitorLog

