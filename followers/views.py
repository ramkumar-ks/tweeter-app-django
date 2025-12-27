from django.shortcuts import render
from .models import Follower
from .serializers import FollowerSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from user.views import UserSearchView
# Create your views here.

class FollowerView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        user_name = user.username
        followers = Follower.objects.filter(user=user, is_following=1).count()
        return Response({'username':user_name, 'followers': followers})

    def post(self, request):
        user = request.user
        user_name = user.username
        obj = UserSearchView()
        user_id = obj.get(request)
        follower_user_id = user_id.data.get('user_id')
        insert_follower, created = Follower.objects.get_or_create(user=user, follower_user_id=follower_user_id, is_following=True)
        if created:
            return Response({'status': 'Followed sucessfully', 'user': user_name, 'follower_user_id': follower_user_id})
        else:
            insert_follower.is_following = False
            insert_follower.save()
            return Response({'status': 'Unfollowed sucessfully', 'user': user_name, 'follower_user_id': follower_user_id})
