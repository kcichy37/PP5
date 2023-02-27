from django.contrib import admin
from .models import Enquiry


class EnquiryAdmin(admin.ModelAdmin):
    """
    Admin view for enquires
    """

    fields = (
        "full_name",
        "email",
        "subject",
        "description",
        "image",
        "resolved",
    )

    list_display = (
        "full_name",
        "email",
        "subject",
        "created_on",
        "resolved",
    )

    ordering = ("-created_on",)


admin.site.register(Enquiry, EnquiryAdmin)
