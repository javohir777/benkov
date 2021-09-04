from django.db import models

# Create your models here.
class contest(models.Model):
    name = models.TextField()
    imageUrl = models.TextField()
    description = models.TextField()
    prize = models.TextField()
    info = models.TextField()
    
class News(models.Model):
    name = models.TextField()
    imageUrl = models.TextField()
    description = models.TextField()
    info = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

      