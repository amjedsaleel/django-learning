from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from . models import Profile

User = settings.AUTH_USER_MODEL


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.create(user=instance, age=30)
        print("Profile is created")


@receiver(post_save, sender=User)
def update_profile(sender, instance, created, *args, **kwargs):
    if not created:
        print("Profile updated")
