from rest_framework import serializers
from django.contrib.auth import get_user_model

class CreateUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True, style={"input_type": "password"})
    email = serializers.EmailField()

    class Meta:
        model = get_user_model()
        fields = [
            'username',
            'password',
            'first_name',
            'last_name',
            'email',
        ]
        write_only_fields = [
            "password",
        ]
        read_only_fields = [
            "is_staff",
            "is_superuser",
            "is_active",
        ]
    
    def validate_username(self, username):
        if get_user_model().objects.filter(username=username).exists():
            raise serializers.ValidationError("User with username {} already exists.".format(username))
        return username

    def validate_email(self, email):
        if get_user_model().objects.filter(email=email).exists():
            raise serializers.ValidationError("User with email {} already exists.".format(email))
        return email
    
    def create(self, validated_data):
        user = super(CreateUserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user