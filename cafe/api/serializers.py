from rest_framework import serializers
from cafe.models import Cafe
from address.models import Address

class CafeSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    address1 = serializers.SerializerMethodField()
    address2 = serializers.SerializerMethodField()
    
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
        ]
    def get_address1(self, obj):
        return obj.address1.formatted

    def get_address2(self, obj):
        return obj.address2.formatted if obj.address2 else obj.address2

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = [
            'formatted'
        ]