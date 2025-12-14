from rest_framework import serializers
from .models import User
from django.contrib.auth.password_validation import validate_password

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
        password = validated_data.pop("password")
        u = User(**validated_data)
        u.set_password(password)
        u.save()
        return u
    