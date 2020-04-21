from rest_framework import serializers
from .models import Board

class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ( part, version, passfail, checkcnt, defectcnt)
        model = Board