from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<int:id>/', views.detail, name='detail'),
]
