from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Phone(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_no = models.CharField(max_length=10)

    def __str__(self):
        return self.phone_no



