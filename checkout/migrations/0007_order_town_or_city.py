# Generated by Django 3.2 on 2023-02-26 19:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("checkout", "0006_alter_order_postcode"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="town_or_city",
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
    ]
