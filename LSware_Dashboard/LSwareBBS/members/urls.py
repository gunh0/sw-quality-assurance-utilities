from rest_framework import routers
from .api import MembersViewSet
 
router = routers.DefaultRouter()
router.register('api/members', MembersViewSet, 'members')
 
urlpatterns = router.urls