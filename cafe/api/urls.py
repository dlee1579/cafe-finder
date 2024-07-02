from rest_framework import routers
from cafe.api.views import CafeViewSet

router = routers.SimpleRouter()
router.register(r'', CafeViewSet, basename='cafes')

urlpatterns = []

urlpatterns += router.urls