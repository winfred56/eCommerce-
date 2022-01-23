from django.db import models
from django.contrib.auth.models import User
# Install pillow to use PIL
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    #uploads all the profile picture images to 'profile_imgs' folder
    profile_img = models.ImageField(upload_to='profile_imgs', default='default.jpg')

    def __str__(self):
        return f"{self.user.username}'s profile"

    # before saving the image, gets the images and changes the size of the image
    def save(self):
        super().save()

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)