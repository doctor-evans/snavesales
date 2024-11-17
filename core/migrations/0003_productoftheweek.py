# Generated by Django 5.1.3 on 2024-11-15 19:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_delete_tag_remove_category_id_remove_vendor_id_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProductOfTheWeek",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="product",
                        to="core.product",
                    ),
                ),
            ],
        ),
    ]