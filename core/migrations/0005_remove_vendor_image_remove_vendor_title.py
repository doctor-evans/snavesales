# Generated by Django 5.1.3 on 2024-11-17 07:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_remove_vendor_cover_image_vendor_is_active_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="vendor",
            name="image",
        ),
        migrations.RemoveField(
            model_name="vendor",
            name="title",
        ),
    ]
