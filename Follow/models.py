from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class UserFollowing(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "following")
    following_user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "followers")
    created = models.DateTimeField(auto_now_add=True)