from django.db import models

# Create your models here.
class Registration(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    
    def __str__(self):
        return self.username