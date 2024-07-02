from rest_framework import routers
from reviews.api.views import ReviewViewSet

router = routers.SimpleRouter()
router.register(r'', ReviewViewSet, basename='reviews')
# router.register(r'cafe/(?P<cafe_id>[0-9]+)', ReviewViewSet, basename='reviews-cafe')
# router.register(r'author/(?P<author_id>[0-9]+)', ReviewViewSet, basename='reviews-author')
# router.register(r'cafe/', ReviewViewSet, basename='list_reviews')

urlpatterns = []

urlpatterns += router.urls