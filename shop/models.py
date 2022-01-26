from itertools import product
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Product(models.Model):
    name = models.CharField(max_length=255)
    feature_image = models.ImageField(upload_to='images/')
    description = models.TextField()
    price = models.DecimalField(decimal_places=3, max_digits=10000)

    def __str__(self):
        return self.name

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product.name}'s image"

class Color(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.product.name}' color"

class Size(models.Model):
    product = models.ForeignKey(Product ,on_delete=models.CASCADE)
    size = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.product.name}' size"

class CartItem(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    ordered = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"

class Cart(models.Model):
    user =models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(CartItem)
    ordered = models.BooleanField(default=False)
    #ordered_date = models.DateTimeField(timezone.now)

    def __str__(self):
        return self.user.username
