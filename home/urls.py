from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('add_reviews/', views.add_reviews, name='add_reviews'),
    path('delete/<int:reviews_id>/', views.delete_review, name='delete_review'),
]
