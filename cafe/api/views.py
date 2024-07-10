from rest_framework import viewsets
from cafe.api.serializers import CafeSerializer
from cafe.models import Cafe
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication

class CafeViewSet(viewsets.ModelViewSet):
    serializer_class = CafeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = (TokenAuthentication,) 

    
    def get_queryset(self):
        return Cafe.objects.all()
    
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)