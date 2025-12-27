from django.urls import path
from .views import TweetViewSet, Timeline

tweet_url = TweetViewSet.as_view()
timeline = Timeline.as_view()
urlpatterns = [
    path('tweets/', tweet_url, name='tweets'),
    path('timeline/', timeline, name='timeline'),
]
