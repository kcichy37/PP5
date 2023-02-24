from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import FoodProduct, FoodCategory
from .forms import ProductForm
from django.contrib import messages
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
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid')
    else:
        form = ProductForm()

    template = 'menu/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
