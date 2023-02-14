from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_food_products, name='menu'),
]
