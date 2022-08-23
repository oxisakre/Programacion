from datetime import date
from datetime import datetime
from django.db import models

# Create your models here.

from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Gender(models.Model):
    GENDER_TYPE = (
        ('M', 'Masculine'),
        ('F', 'Feminine'),
        ('O', 'Other'),
    )
    name = models.CharField(max_length=1, choices=GENDER_TYPE)

    def __str__(self):
        return self.name


class Identification(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    birthdate = models.DateTimeField()
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)