from rest_framework import serializers
from api.models import Posts
from django.contrib.auth.models import User

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Posts
        exclude=("date",)
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["first_name","last_name","email","username","password"]

def create(self,validated_data):
    return User.objects.create_user(**validated_data)


