# Generated by Django 5.1.3 on 2024-11-16 01:06

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_productoftheweek"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="vendor",
            name="cover_image",
        ),
        migrations.AddField(
            model_name="vendor",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="vendor",
            name="image",
            field=models.ImageField(
                default="vendor.jpg", upload_to=core.models.user_directory_path
            ),
        ),
    ]
