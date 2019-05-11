from django.db import models

# Create your models here.
class Movies(models.Model):
    movieId = models.IntegerField()
    title = models.CharField(max_length=50)
    genres = models.CharField(max_length=100)