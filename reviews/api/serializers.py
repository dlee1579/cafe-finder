from rest_framework import serializers
from cafe.models import Cafe
from reviews.models import Review
from django.contrib.auth import get_user_model
from reviews.constants import rating_fields

class ReviewSerializer(serializers.ModelSerializer):
    author_id = serializers.PrimaryKeyRelatedField(queryset=get_user_model().objects.all(), many=False, source='author', required=False)
    cafe_id = serializers.PrimaryKeyRelatedField(queryset=Cafe.objects.all(), many=False, source='cafe')
    
    class Meta:
        model = Review
        fields = [
            'id',
            'author_id',
            'cafe_id',
            'title',
            'description',
            'coffee_quality',
            'comfortability',
            'atmosphere',
            'quietness',
            'cleanliness',
            'created_at',
            'updated_at',
        ]
        read_only_fields = [
            'id',
            'author_id',
            'title',
            'description',
            'created_at',
            'updated_at',
        ]

    def validate_coffee_quality(self, coffee_quality):
        if coffee_quality > 5 or coffee_quality < 1:
            raise serializers.ValidationError("Coffee quality rating must be between 1 and 5.")
        return coffee_quality
    
    def validate_comfortability(self, comfortability):
        if comfortability > 5 or comfortability < 1:
            raise serializers.ValidationError("Comfortability rating must be between 1 and 5.")
        return comfortability

    def validate_atmosphere(self, atmosphere):
        if atmosphere > 5 or atmosphere < 1:
            raise serializers.ValidationError("Atmosphere rating must be between 1 and 5.")
        return atmosphere
    
    def validate_quietness(self, quietness):
        if quietness > 5 or quietness < 1:
            raise serializers.ValidationError("Quietness rating must be between 1 and 5.")
        return quietness
    
    def validate_cleanliness(self, cleanliness):
        if cleanliness > 5 or cleanliness < 1:
            raise serializers.ValidationError("Cleanliness rating must be between 1 and 5.")
        return cleanliness
    
    def create(self, validated_data,):
        # author = validated_data.get("author")
        cafe = validated_data.get('cafe')
        
        method = self.context.get('method')
        user = self.context.get('user')
        if method == "POST":
            if Review.objects.filter(author=user, cafe=cafe).exists():
                raise serializers.ValidationError("Review for this cafe from this user already exists.")
            return Review.objects.create(**validated_data)
        elif method == "PUT":
            review = Review.objects.get(id=self.context.get('id'))
            if not review:
                raise serializers.ValidationError("Review with the provided id does not exist.")
            for field, value in validated_data.items():
                setattr(review, field, value)
            review.save()
            return review
