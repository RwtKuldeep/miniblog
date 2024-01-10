from django.db import models

# Create your models here.


class User_Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    address = models.TextField()
    message = models.TextField()


class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
