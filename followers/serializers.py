from rest_framework.serializers import ModelSerializer
from .models import Follower
from django.contrib.auth.models import User

class FollowerSerializer(ModelSerializer):
    class Meta:
        table = Follower
        fields = ['follower_user_id', 'is_following']