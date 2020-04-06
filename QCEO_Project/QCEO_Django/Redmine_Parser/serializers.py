from rest_framework import serializers
from .models import RedPaser

class RedPaserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'num',
            'project',
            'category',
            'state',
            'priority', 
            'title', 
            'author', 
            'master',
            'change', 
            'start',
        )
        model = RedPaser