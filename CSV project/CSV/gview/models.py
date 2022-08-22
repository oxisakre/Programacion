from django.db import models

# Create your models here.

from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Genre(models.Model):
    GENRE_TYPE = (
        ('M', 'Masculine'),
        ('F', 'Feminine'),
        ('O', 'Other'),
    )
    genre_type = models.CharField(max_length=1, choices=GENRE_TYPE)

    def __str__(self):
        return self.genre_type

class Birthdate(models.Model):
    name = models.DateTimeField(max_length=3)

    def __str__(self):
        return self.name

class Identification(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    birthdate = models.ForeignKey(Birthdate, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)