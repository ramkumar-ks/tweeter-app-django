from django.core.serializers import serialize
from django.shortcuts import render
from rest_framework import status

from .models import Tweet
from.serializers import TweetSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from comments.views import get_comments
from likes.views import get_likes
from django.contrib.auth.models import User
# Create your views here.

class TweetViewSet(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        tweets = Tweet.objects.filter(user=user)
        serializer = TweetSerializer(tweets, many=True)
        tweets = []
        for tweet in serializer.data:
            tweet['user'] = user.username
            id = tweet.pop('id')
            likes = get_likes(id)
            if likes:
                tweet['likes'] = likes.data.get('likes')
            comments_data = get_comments(request, id)
            if comments_data.data:
                tweet['comments'] = comments_data.data
            tweets.append(tweet)
        return Response({'tweets': tweets})

    def post(self, request):
        user = request.user
        request_dict = {}
        if request.data.get('tweet_content'):
            request_dict['tweet_content'] = request.data.get('tweet_content')
        if request.data.get('likes'):
            request_dict['likes'] = request.data.get('likes')
        if request.data.get('comments'):
            request_dict['comments'] = request.data.get('comments')
        insert_tweet, created = Tweet.objects.get_or_create(user=user, **request_dict)
        if created:
            insert_tweet.save()
            return Response({'tweet_content': insert_tweet.tweet_content}, status=status.HTTP_201_CREATED)
        else:
            return Response({'Error': "Invalid data"}, status=status.HTTP_400_BAD_REQUEST)


class Timeline(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user.id
        tweets = Tweet.objects.extra(
            tables=["followers_follower"],
            where=["tweet_tweet.user_id = followers_follower.follower_user_id",
                   "followers_follower.user_id = %s", "followers_follower.is_following = TRUE"],
            params=[user],
            order_by=["-tweet_tweet.created_at"]
        )
        data = []
        for t in tweets:
            user_id = User.objects.filter(id=t.user_id).first()
            data.append({
                "user_name": user_id.username,
                "tweet_content": t.tweet_content,
                "likes": t.likes,
                "comments": t.comments,
                "created_at": t.created_at
            })
        print(tweets)
        return Response({'tweets': data})

