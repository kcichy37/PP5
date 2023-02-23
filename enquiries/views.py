from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import EnquiryForm
from .models import Enquiry


def enquiry(request):
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            enquiry = form.save()
            send_mail(
                f"New enquiry from {enquiry.full_name} at {enquiry.email}",
                f"{enquiry.subject}\n\n{enquiry.description}",

                "noreply@tasteofitaly.com",
                ["tasteofitalyproject@gmail.com"],
                fail_silently=False,
            )
            return redirect('enquiry_success')
    else:
        form = EnquiryForm()

    return render(request, 'enquiry.html', {'form': form})


def enquiry_success(request):
    return render(request, 'enquiry_success.html')
