from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        Fields = ('id', 'username', 'email', 'phone', 'address')
        read_only = ['id']