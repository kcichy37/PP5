from django.contrib import admin
from .models import FoodProduct, FoodCategory


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'image_url',
        'image',
    )

    ordering = ('category',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'friendly_name',
        'name',
    )


admin.site.register(FoodProduct, ProductAdmin)
admin.site.register(FoodCategory, CategoryAdmin)
