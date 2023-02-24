from django.urls import path
from . import views

urlpatterns = [
    path('', views.food_menu, name='menu'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>', views.delete_product, name='delete_product'),
    path('all_products/', views.all_products, name='all_products'),
]
