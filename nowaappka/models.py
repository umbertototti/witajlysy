from django.db import models

# Create your models here.
class nowaappka(models.Model):
    title = models.TextField()
    description = models.TextField()
    price = models.TextField()
    summary = models.TextField(default='this is cool')
