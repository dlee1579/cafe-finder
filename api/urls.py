from django.urls import include, path

urlpatterns = [
    path('cafe/', include("cafe.api.urls")),
    path('auth/', include("auth.api.urls")),
    path('reviews/', include("reviews.api.urls")),
]