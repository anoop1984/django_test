from rest_framework import serializers
from .models import healthCheck



class healthCheckSerializer(serializers.Serializzer);
    desc = serializers.CharField(max_length = 264)
    severity =        serializers.CharField(max_length = 50)
    ipaddr       = serializers.GenericIPAddressField()
    hostname =        serializers.CharField(max_length = 100)
    command = serializers.CharField(max_length = 264)
    verdict =         serializers.CharField(max_length = 264)
    remarks  =         serializers.CharField(max_length = 1000)
    test_id =          serializers.CharField(max_length = 100)
    date =            serializers.DateField()


    def create(self, validated_data):
        return healthCheck.objects.create(validated_data)
~                                           
