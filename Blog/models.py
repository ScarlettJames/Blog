from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=20)
    body = models.TextField()
    post_created = models.DateField(default=date.today)
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True)