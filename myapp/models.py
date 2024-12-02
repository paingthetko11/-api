from django.db import models

# Create your models here.
class Home(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    cv = models.FileField(null=True,blank=True)
    image = models.ImageField(upload_to='images/')
    facebook = models.URLField(max_length=500)
    github = models.URLField(max_length=500)
    telegram = models.URLField(max_length=500)
    discord = models.URLField(max_length=500)