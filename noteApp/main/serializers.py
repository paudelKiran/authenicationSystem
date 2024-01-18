from main.models import User,Profile
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email','password','date_created']


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"

class LoginSerializer(serializers.Serializer):
    email=serializers.EmailField()
    password=serializers.CharField()
