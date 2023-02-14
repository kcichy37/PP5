from django.shortcuts import render
from .models import FoodProduct
# Create your views here.


def food_menu(request):
    """
    A view to show the food products
    """
    food_products = FoodProduct.objects.all()

    context = {
        'food_products': food_products,
    }

    return render(request, 'menu/menu.html')
