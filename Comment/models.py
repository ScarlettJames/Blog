from django.contrib.auth.models import User
from Blog.models import Blog
from django.db import models

# Create your models here.
class CommentModel(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True)
    comment = models.TextField()