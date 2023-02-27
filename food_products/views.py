from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import FoodProduct, FoodCategory
from .forms import ProductForm


def food_menu(request):
    """
    A view to show the food products
    """
    products = FoodProduct.objects.all()

    context = {"products": products}

    return render(request, "menu/menu.html", context)


@login_required
def all_products(request):
    """
    A view to show all the products for edit and delete
    """
    if not request.user.is_superuser:
        messages.error(request, "You dont have permission to enter this page.")
        return redirect(reverse("home"))

    products = FoodProduct.objects.all()

    context = {"products": products}

    return render(request, "menu/all_products.html", context)


@login_required
def add_product(request):
    """
    Add a product to the store
    """
    if not request.user.is_superuser:
        messages.error(request, "You dont have permission to enter this page.")
        return redirect(reverse("home"))

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully added product!")
            return redirect(reverse("all_products"))
        else:
            messages.error(
                request, "Failed to add product. Please ensure the form is valid"
            )
    else:
        form = ProductForm()

    template = "menu/add_product.html"
    context = {
        "form": form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """
    Edit a product in the store
    """
    if not request.user.is_superuser:
        messages.error(request, "You dont have permission to enter this page.")
        return redirect(reverse("home"))

    product = get_object_or_404(FoodProduct, pk=product_id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f"Successfully edited {product.name}")
            return redirect(reverse("all_products"))
        else:
            messages.error(
                request,
                f"Failed to update {product.name}. Please ensure the form is valid",
            )
    else:
        form = ProductForm(instance=product)
        messages.info(request, f"You are editing {product.name}")

    template = "menu/edit_product.html"
    context = {"form": form, "product": product}

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """
    Delete a product
    """
    if not request.user.is_superuser:
        messages.error(request, "You dont have permission to enter this page.")
        return redirect(reverse("home"))

    product = get_object_or_404(FoodProduct, pk=product_id)
    product.delete()
    messages.success(request, f"Product {product.name} deleted successfully.")
    return redirect(reverse("all_products"))
