from django.contrib import admin
from .models import Cart ,CartItem, Product, Image, Color, Size

admin.site.register(Product)
admin.site.register(Image)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Cart)
admin.site.register(CartItem)
