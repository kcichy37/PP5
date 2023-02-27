from django.contrib import admin
from .models import FoodProduct, FoodCategory


# Register your models here.
class FoodProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "price",
        "image_url",
        "image",
    )

    ordering = ("category",)


class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "friendly_name",
        "name",
    )


admin.site.register(FoodProduct, FoodProductAdmin)
admin.site.register(FoodCategory, FoodCategoryAdmin)
