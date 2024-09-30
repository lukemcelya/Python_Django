from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=100, blank=True)
    entry = models.TextField(max_length=500)
    date = models.DateField()
    