from django.db import models


class Fashionista(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    fb = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    blog = models.URLField(blank=True)
    desc = models.TextField()