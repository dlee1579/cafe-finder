from rest_framework import viewsets
from cafe.api.serializers import CafeSerializer
from cafe.models import Cafe
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly

class CafeViewSet(viewsets.ModelViewSet):
    serializer_class = CafeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get_queryset(self):
        return Cafe.objects.all()