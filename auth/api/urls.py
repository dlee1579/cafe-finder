from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import CreateUserAPIView, LogoutUserAPIView


urlpatterns = [
    path(r'login/',
        obtain_auth_token,
        name='auth_user_login'),
    path(r'register/',
        CreateUserAPIView.as_view(),
        name='auth_user_create'),
    path(r'logout/',
        LogoutUserAPIView.as_view(),
        name='auth_user_logout')
]