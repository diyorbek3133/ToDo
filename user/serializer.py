from rest_framework.serializers import ModelSerializer
from .models import User
from rest_framework import serializers
from rest_framework.authentication import authenticate


class UserRegisterSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ["username","password"]
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"]
        )
        return user
    
class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    
    def validate(self, data):
        user = authenticate(**data)
        if not user:
            raise serializers.ValidationError("user or password error")
        data["user"] = user
        return data
"test"