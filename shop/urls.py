from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<int:id>/', views.detail, name='detail'),
    path('add/<int:id>/', views.add, name='add'),
    path('remove/<int:id>/', views.remove, name='remove'),
]
