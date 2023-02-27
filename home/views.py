from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Reviews
from .forms import ReviewForm

# Create your views here.


def index(request):
    """
    View for home page
    """
    reviews = Reviews.objects.all()

    context = {"reviews": reviews}
    return render(request, "home/index.html", context)


@login_required
def add_reviews(request):
    """
    Handles add reviews view
    """
    reviews = Reviews.objects.all()

    if request.method == "POST":
        form = ReviewForm(request.POST, user=request.user)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            messages.success(request, "Successfully added a review!")
            return redirect(reverse("add_reviews"))
        else:
            messages.error(
                request, "Failed to add product. Please ensure the form is valid"
            )
    else:
        form = ReviewForm(user=request.user)

    context = {
        "form": form,
        "reviews": reviews,
    }

    return render(request, "home/reviews.html", context)


@login_required
def delete_review(request, reviews_id):
    """
    Enables users to delete their reviews
    """
    reviews = get_object_or_404(Reviews, pk=reviews_id)

    if request.user.is_superuser:
        reviews.delete()
        messages.success(request, "The review has been deleted")
        return redirect(reverse("add_reviews"))
    elif request.user == reviews.user:
        reviews.delete()
        messages.success(request, "The review has been deleted")
    else:
        messages.error(request, "You do not have permission to remove this review.")

    return redirect(reverse("add_reviews"))
