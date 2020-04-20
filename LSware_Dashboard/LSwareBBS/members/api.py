from members.models import Members
from rest_framework import viewsets, permissions
from .serializers import MembersSerializer
 
class MembersViewSet(viewsets.ModelViewSet):
    queryset = Members.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = MembersSerializer