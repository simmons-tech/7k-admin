from django.db import models
from django.conf import settings

# Create your models here.
class Pic(models.Model):
    # Filepath relative to settings.PICS_ROOT
    filepath = models.FilePathField(path=settings.PICS_ROOT, recursive=True)
    title = models.CharField(max_length=300)
    creator = models.CharField(max_length=32)
    approved = models.BooleanField(default=False)
