from django.urls import path
from . import views

urlpatterns = [
    path('', views.food_menu, name='menu'),
    path('add/', views.add_product, name='add_product'),
]
