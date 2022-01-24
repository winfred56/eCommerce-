from dataclasses import Field
from itertools import product
from pyexpat import model
from random import choice
from ssl import Options
from turtle import color
from django.db import models

class Color(models.Model):
    color = models.CharField(max_length=100, null=True, blank= True)

class Size(models.Model):
    size = models.CharField(max_length=100, null=True, blank=True)

class Product(models.Model):
    name = models.CharField(max_length=255)
    feature_image = models.ImageField(upload_to='images/')
    other_images = models.ForeignKey('Image', related_name='product_images', on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(decimal_places=3, max_digits=10000)
    color = models.ForeignKey(Color, null=True, on_delete=models.SET_NULL)
    size = models.ForeignKey(Size, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField(upload_to='images/')


