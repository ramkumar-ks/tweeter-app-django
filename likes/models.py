from django.db import models
from django.contrib.auth.models import User
from tweet.models import Tweet

# Create your models here.

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    likes = models.IntegerField()
    is_liked = models.BooleanField(default=False)

    def __str__(self):
        return self.likes, self.is_liked