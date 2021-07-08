from django.db import models

# Create your models here.
class Movie(models.Model):

  movie_id = models.CharField(max_length=10)
  title = models.CharField(max_length=144)
  overview = models.CharField(max_length=300)
  poster = models.CharField(max_length=144)
  vote_average = models.CharField(max_length=10)
  vote_count = models.CharField(max_length=10)