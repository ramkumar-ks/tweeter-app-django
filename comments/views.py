from django.shortcuts import render

from .models import Comment
from tweet.models import Tweet
from .serializers import CommentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class CommentViewSet(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, id):
        user = request.user
        comments = Comment.objects.filter(user=user, tweet=id)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, id):
        user = request.user
        comments = request.data.get('comment')
        comment, created = Comment.objects.get_or_create(user=user, tweet_id=id, comment=comments)
        if created:
            comment.save()
            return Response({'comment':comments}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error':'invalid data'}, status=status.HTTP_400_BAD_REQUEST)

def get_comments(request, id):
    user = request.user
    comments = Comment.objects.filter(user=user, tweet=id)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)