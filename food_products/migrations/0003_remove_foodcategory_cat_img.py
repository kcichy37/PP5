# Generated by Django 3.2 on 2023-02-18 20:12

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("food_products", "0002_auto_20230218_2001"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="foodcategory",
            name="cat_img",
        ),
    ]
