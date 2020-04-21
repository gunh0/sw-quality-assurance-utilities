from rest_framework import routers

from .views import BoardViewSet

router = routers.DefaultRouter()
router.register('boards', BoardViewSet, 'boards')

urlpatterns = router.urls