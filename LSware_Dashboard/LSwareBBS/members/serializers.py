from rest_framework import serializers
from members.models import Members
 
class MembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = '__all__'