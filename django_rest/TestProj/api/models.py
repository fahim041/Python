from django.db import models
from django.db.models.deletion import SET_NULL
from django.db.models.fields import NullBooleanField

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Release(models.Model):
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.city
