from django.shortcuts import render
from .models import FoodProduct, FoodCategory
from .forms import ProductForm
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


def add_product(request):
    """
    Add a product to the store
    """
    form = ProductForm()
    template = 'menu/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
