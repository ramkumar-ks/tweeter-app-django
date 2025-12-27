from django.db import models
from django.contrib.auth.models import User
from followers.models import Follower
# Create your models here.

class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet_content = models.TextField()
    likes = models.IntegerField(default=0)
    comments = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tweet_content, self.likes, self.comments, self.created_at