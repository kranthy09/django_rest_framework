from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(max_length=191, unique=True)
    email = models.EmailField(blank=True)
    password = models.CharField(max_length=100)
    is_superuser = models.BooleanField(default=False)


class Post(models.Model):
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    posted_at = models.DateTimeField(auto_now=True)
    post_content = models.CharField(max_length=200)
