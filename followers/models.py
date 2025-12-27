from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Follower(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    follower_user_id = models.IntegerField()
    is_following = models.BooleanField(default=False)

    def __str__(self):
        return self.follower_user_id, self.is_following

