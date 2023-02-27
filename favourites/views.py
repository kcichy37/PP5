from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from food_products.models import FoodProduct
from .models import Favourite


@login_required
def my_favourites(request):
    """
    Handles my favourite page view
    """
    favourites = Favourite.objects.filter(user=request.user)

    context = {"favourites": favourites}
    return render(request, "favourites/favourites.html", context)


@login_required
def add_to_favourites(request, product_id):
    """
    Enables adding favourites to the
    favourties page
    """
    product = get_object_or_404(FoodProduct, pk=product_id)
    favourite, created = Favourite.objects.get_or_create(
        user=request.user, product=product
    )
    if created:
        messages.success(request, f"{product.name} has been added to your favourites.")
    else:
        messages.error(request, f"{product.name} is already in your favourites.")

    context = {"product": product, "favourite": favourite}
    return redirect(reverse("menu"))


@login_required
def delete_favourites(request, favourite_id):
    """
    Enables removal of favourties
    """
    favourite = get_object_or_404(Favourite, pk=favourite_id)
    if request.user == favourite.user:
        favourite.delete()
        messages.success(
            request, f"{favourite.product.name} has been removed from your favourites."
        )
    else:
        messages.error(
            request,
            "You do not have permission to remove this product from your favourites.",
        )

    return redirect(reverse("my_favourites"))
