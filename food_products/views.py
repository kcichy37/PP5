from django.shortcuts import render
from .models import FoodProduct, FoodCategory
# Create your views here.


def food_menu(request):
    """
    A view to show the food products
    """
    product = FoodProduct.objects.all()

    starters = FoodProduct.objects.filter(category='1')
    salads = FoodProduct.objects.filter(category='2')
    pizza = FoodProduct.objects.filter(category='3')
    pasta = FoodProduct.objects.filter(category='4')
    risotto = FoodProduct.objects.filter(category='5')
    meat_fish = FoodProduct.objects.filter(category='7')
    sides = FoodProduct.objects.filter(category='8')
    desserts = FoodProduct.objects.filter(category='9')
    soft_drinks = FoodProduct.objects.filter(category='10')

    context = {
        'starters': starters,
        'salads': salads,
        'pizza': pizza,
        'pasta': pasta,
        'risotto': risotto,
        'meat_fish': meat_fish,
        'sides': sides,
        'desserts': desserts,
        'soft_drinks': soft_drinks,
        'product': product,
    }

    return render(request, 'menu/menu.html', context)
