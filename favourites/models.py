from django.db import models
from food_products.models import FoodProduct
from django.contrib.auth.models import User


# Create your models here.
class Favourite(models.Model):
    """
    Model for favourites
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(FoodProduct, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} likes {self.product.name}"
