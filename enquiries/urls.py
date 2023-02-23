from django.urls import path
from . import views

urlpatterns = [
    path('', views.enquiry, name='enquiry'),
    path('enquiry_success/', views.enquiry_success, name='enquiry_success'),
]
