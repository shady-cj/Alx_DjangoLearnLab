from rest_framework import serializers
from .models import User
from django.contrib.auth.password_validation import validate_password
# "from rest_framework.authtoken.models import Token", "serializers.CharField()", "Token.objects.create", "get_user_model().objects.create_user"

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "email", "username", "followers", "following", "bio"]



class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name"
            "email",
            "username",
            "password",
            "confirm_password"
        ]
    
    def validate(self, attrs):
        password = attrs.get("password")
        confirm_password = attrs.get("confirm_password")
        validate_password(password)
        if password != confirm_password:
            raise serializers.ValidationError("Password mismatch")
        
        attrs.pop("confirm_password")
        return super().validate(attrs)
        
    def create(self, validated_data):
        u = User.objects.create_user(**validated_data)
        return u
    