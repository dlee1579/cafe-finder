from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from cafe.models import Cafe
from reviews.api.serializers import ReviewSerializer
from reviews.models import Review

class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get_queryset(self):
        query_fields = ['cafe_id', 'author_id']
        
        cafe_id = self.request.query_params.get('cafe_id')
        author_id = self.request.query_params.get('author_id')
        
        
        kwargs = {}
        for query_field in query_fields:
            field_value = self.request.query_params.get(query_field)
            if field_value:
                kwargs.update({query_field: field_value})
        if not kwargs:
            return []
        return Review.objects.filter(**kwargs)
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({
            "request": self.request,
        })
        return context

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        context = self.get_serializer_context().update({"method": "POST"})
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
            
    def partial_update(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    
    def update(self, request, *args, **kwargs):
        data = request.data
        context = self.get_serializer_context()
        context.update({"method": "PUT", "id": kwargs.get("pk")})
        serializer = self.serializer_class(data=data, context=context,)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)