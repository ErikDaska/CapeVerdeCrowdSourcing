from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

# Create your models here.
class Phrases(models.Model):
    portuguese = models.CharField(max_length=1000)
    creoule = models.JSONField(default=list)
    id = models.AutoField(primary_key=True)


