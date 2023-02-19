from django.shortcuts import render
from .models import FoodProduct, FoodCategory
# Create your views here.


def food_menu(request):
    """
    A view to show the food products
    """
    products = FoodProduct.objects.all()

    context = {
        'products': products
    }

    return render(request, 'menu/menu.html', context)



