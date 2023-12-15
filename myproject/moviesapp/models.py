from django.db import models

# Create your models here.
class Movies(models.Model):
    moviename = models.CharField(max_length=100)
    heroname = models.CharField(max_length=100)
    heroinename = models.CharField(max_length=100)
    