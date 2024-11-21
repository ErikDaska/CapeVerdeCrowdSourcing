from django.db import models

# Create your models here.
class Phrases(models.Model):
    portuguesePhrase = models.CharField(max_length=1000)
    translatedPhrase = models.CharField(max_length=1000)
