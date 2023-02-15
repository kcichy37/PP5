from django.shortcuts import render
from .models import FoodProduct, FoodCategory
# Create your views here.


def food_menu(request):
    """
    A view to show the food products
    """
    starters = FoodProduct.objects.filter(category='1')

    context = {
        'starters': starters,
    }

    return render(request, 'menu/menu.html', context)
