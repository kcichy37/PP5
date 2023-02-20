from django.shortcuts import render, redirect
from django.http import JsonResponse


# Create your views here.
def view_bag(request):
    """
    View for the checkout bag
    """
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """
    Add product to the bag
    """
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity'))
        bag = request.session.get('bag', {})
        redirect_url = request.POST.get('redirect_url')

        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

        request.session['bag'] = bag

        # Create a JSON response that includes the updated bag data
        response_data = {
            'success': True,
            'bag': bag
        }
        return JsonResponse(response_data)
