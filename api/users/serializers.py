from django.contrib.auth import authenticate
from rest_framework import serializers

from users.models import User


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data) -> User:
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["email", "password"]

    def create(self, validated_data) -> User:
        user = User.objects.create_user(
            email=validated_data["email"], password=validated_data["password"]
        )
        return user
