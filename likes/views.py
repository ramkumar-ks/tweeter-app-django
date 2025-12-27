from django.shortcuts import render
from .models import Like
from .serializers import LikeSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, viewsets


# Create your views here.
class LikeViewSet(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, id):
        likes = Like.objects.filter(tweet_id=id).count()
        user_like = Like.objects.filter(tweet_id=id, user=request.user)
        if user_like:
            user_like.delete()
            return Response({'likes': Like.objects.filter(tweet_id=id).count()})
        else:
            like, created = Like.objects.get_or_create(user=request.user, tweet_id=id, likes= likes+1 ,is_liked=True)
            if created:
                return Response({'likes': like.likes}, status=status.HTTP_201_CREATED)
            else:
                return Response({'error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)

def get_likes(id):
    likes = Like.objects.filter(tweet_id=id).count()
    return Response({'likes': likes})
