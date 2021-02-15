from django.db import models

# Create your models here.


class Example(models.Model):
    name = models.CharField(max_length=40)
    location = models.CharField(max_length=40)

    def __str__(self):
        return self.name