from rest_framework import serializers
from .models import *

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
   
        model = Video
        fields = '__all__'
        read_only_fields = ['transcript', 'notes', 'processed', 'error_message', 'created_at']
   