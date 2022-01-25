from django.db import models
from django.contrib.auth.models import User
# Install pillow to use PIL
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    #uploads all the profile picture images to 'profile_imgs' folder
    profile_img = models.ImageField(upload_to='profile_imgs', default='default/default.jpg')

    def __str__(self):
        return f"{self.user.username}'s profile"

    # before saving the image, gets the images and changes the size of the image
    #def save(self):
    #    super().save()
#
    #    img = Image.open(self.profile_img.path)
    #    if img.height > 300 or img.width > 300:
    #        output_size = (300,300)
    #        img.thumbnail(output_size)
    #        img.save(self.profile_img.path)

class Address(models.Model):
    address = models.ForeignKey( Profile, on_delete=models.SET_NULL, null=True)
    address_line_1 = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    country = models.CharField(max_length=150)


    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Address'


