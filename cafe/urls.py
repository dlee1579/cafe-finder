from django.urls import include, path
from cafe import views
from cafe.api.views import CafeViewSet
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'cafes', CafeViewSet, basename="cafes")

urlpatterns = [
    path("", views.home, name="home"),
    path("api/", include('cafe.api.urls'))
    # path("api/", include(router.urls)),
]
