# Generated by Django 3.2 on 2023-02-23 19:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("checkout", "0002_auto_20230223_1639"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="postcode",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
