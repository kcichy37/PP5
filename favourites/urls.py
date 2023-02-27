from django.urls import path
from . import views

urlpatterns = [
    path("", views.my_favourites, name="my_favourites"),
    path("add/<int:product_id>", views.add_to_favourites, name="add_to_favourites"),
    path(
        "delete/<int:favourite_id>", views.delete_favourites, name="delete_favourites"
    ),
]
