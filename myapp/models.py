from django.db import models

# Create your models here.


class Article(models.Model):

    Title=models.CharField(max_length=100)
    Description=models.TextField()
    
