from django.db import models

# Create your models here.
class Movies(models.Model):
    movieId = models.IntegerField()
    title = models.CharField(max_length=200)
    genres = models.CharField(max_length=150)
class Links(models.Model):
    movieId = models.IntegerField()
    imdbId = models.IntegerField()
    tmdbId = models.IntegerField()