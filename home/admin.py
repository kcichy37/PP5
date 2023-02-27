from django.contrib import admin
from .models import Reviews


class ReviewsAdmin(admin.ModelAdmin):
    """
    Admin view for enquires
    """

    fields = (
        "user",
        "comment",
        "rating",
    )

    list_display = (
        "user",
        "comment",
        "rating",
        "created_on",
    )

    ordering = ("-created_on",)


admin.site.register(Reviews, ReviewsAdmin)
