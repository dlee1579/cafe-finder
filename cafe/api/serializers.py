from rest_framework import serializers
from cafe.models import Cafe
from address.models import Address
from reviews.models import Review
from django.db.models import Avg

class CafeSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    address1 = serializers.SerializerMethodField()
    address2 = serializers.SerializerMethodField()
    ratings = serializers.SerializerMethodField()
    
    class Meta:
        model = Cafe
        fields = [
            'id',
            'name',
            'address1',
            'address2',
            'number_seats',
            'type_seats',
            'description',
            'neighborhood',
            'has_wall_outlets',
            'is_pet_friendly',
            'thumbnail_image_location',
            'ratings'
        ]
    def get_address1(self, obj):
        return obj.address1.formatted

    def get_address2(self, obj):
        return obj.address2.formatted if obj.address2 else obj.address2
    
    def get_ratings(self, obj):
        ratings = Review.objects.filter(cafe_id=obj.id).aggregate(
            coffee_quality=Avg("coffee_quality"),
            comfortability=Avg("comfortability"),
            atmosphere=Avg("atmosphere"),
            quietness=Avg("quietness"),
            cleanliness=Avg("cleanliness"),
        )
        return ratings

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = [
            'formatted'
        ]

# class RatingSerializer(serializers.ModelSerializer):
    