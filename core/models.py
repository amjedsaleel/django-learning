from django.db import models
from django.conf import settings
# Create your models here.

User = settings.AUTH_USER_MODEL


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField()
    image = models.ImageField()


class BlogPost(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(blank=True, null=True)
    liked = models.ManyToManyField(User, blank=True)
    notify_users = models.BooleanField(default=False)
    notify_users_timestamp = models.DateTimeField(blank=True, null=True, auto_now_add=False)
    active = models.BooleanField(default=True)
