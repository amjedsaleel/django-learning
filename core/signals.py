from django.conf import settings
from django.db.models.signals import post_save, pre_save, pre_delete, post_delete
from django.dispatch import receiver
from django.utils.text import slugify
from . models import Profile, BlogPost

User = settings.AUTH_USER_MODEL


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.create(user=instance, age=30)
        print("Profile is created")


@receiver(post_save, sender=User)
def update_profile(sender, instance, created, *args, **kwargs):
    """
    After User object used in database (past_save)
    """
    if not created:
        print("Profile updated")


@receiver(pre_save, sender=BlogPost)
def blog_handler(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)


@receiver(pre_delete, sender=Profile)
def profile_delete_handler(sender, instance, *args, **kwargs):
    print("Profile will delete")
    print(sender.objects.get(id=instance.id), "..........................")
    instance.image.delete()

