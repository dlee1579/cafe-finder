from rest_framework import viewsets
from cafe.api.serializers import CafeSerializer
from cafe.models import Cafe

class CafeViewSet(viewsets.ModelViewSet):
    serializer_class = CafeSerializer
    
    def get_queryset(self):
        return Cafe.objects.all()