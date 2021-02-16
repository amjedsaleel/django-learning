from django.db import models

# Create your models here.


class Programmer(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.PositiveIntegerField()
    programmer = models.ForeignKey(Programmer, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} " " {self.programmer}'
