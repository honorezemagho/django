from django.db import models
from django.utils import timezone
 
# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=200)
    phone = models.IntegerField()
    email = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    created_at = models.DateField(default=timezone.now)
    updated_at = models.DateField(auto_now=True)