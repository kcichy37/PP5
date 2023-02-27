from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import EnquiryForm
from .models import Enquiry
from django.contrib import messages


def enquiry(request):
    """
    Handles enquiry form view
    """
    email = settings.DEFAULT_FROM_EMAIL

    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            enquiry = form.save()
            messages.success(request, 'Enquiry sent')
            send_mail(
                f"{enquiry.subject}",
                f"Name:{enquiry.full_name}\n\n{enquiry.description}\n\nCreated on:{enquiry.created_on}",

                enquiry.email,
                [email],
                fail_silently=False,
            )
            return redirect('enquiry')
        else:
            messages.error(request, "Enquiry can't be sent")
    else:
        form = EnquiryForm()

    return render(request, 'enquiries/enquiry.html', {'form': form})
