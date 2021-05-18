from django.db import models
from django.contrib.auth.models import User

class wpn(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(default='default.jpg', upload_to='product_pics')


class clt(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(default='default.jpg', upload_to='product_pics')

class fod(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(default='default.jpg', upload_to='product_pics')


    def __str__(self):
        return self.title

