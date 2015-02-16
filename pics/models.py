from django.db import models
from admin7k.settings import PICS_ROOT

# Create your models here.
class Pic(models.Model):
    # Filepath relative to settings.PICS_ROOT
    filepath = models.FilePathField(path='/Users/larsj/Dropbox/Lars/MIT/spring2015/simmons-tech/7k-pics/', recursive=True)
    title = models.CharField(max_length=300)
    creator = models.CharField(max_length=32)
    approved = models.BooleanField(default=False)
