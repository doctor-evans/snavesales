# Generated by Django 5.1.3 on 2024-11-17 18:38

import core.models
import django.db.models.deletion
import shortuuid.django_fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "cid",
                    shortuuid.django_fields.ShortUUIDField(
                        alphabet="abcdefg1234",
                        length=16,
                        max_length=40,
                        prefix="catid_",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("image", models.ImageField(upload_to="category")),
            ],
            options={
                "verbose_name_plural": "categories",
            },
        ),
        migrations.CreateModel(
            name="Product",
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
                    "pid",
                    shortuuid.django_fields.ShortUUIDField(
                        alphabet="abcdefg1234",
                        length=16,
                        max_length=40,
                        prefix="",
                        unique=True,
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("image", models.ImageField(upload_to=core.models.user_directory_path)),
                (
                    "description",
                    models.TextField(default="This is the product description"),
                ),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, default="1.99", max_digits=12
                    ),
                ),
                ("stock_items", models.IntegerField(blank=True, null=True)),
                (
                    "product_status",
                    models.CharField(
                        choices=[
                            ("draft", "Draft"),
                            ("disabled", "Disabled"),
                            ("rejected", "Rejected"),
                            ("in_review", "In Review"),
                            ("published", "Published"),
                        ],
                        default="in_review",
                        max_length=10,
                    ),
                ),
                ("status", models.BooleanField(default=True)),
                ("in_stock", models.BooleanField(default=True)),
                ("featured", models.BooleanField(default=False)),
                ("date", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(blank=True, null=True)),
                (
                    "category",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="products",
                        to="core.category",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProductImages",
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
                ("images", models.ImageField(upload_to="product_images")),
                ("date", models.DateTimeField(auto_now_add=True)),
                (
                    "product",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="productimages",
                        to="core.product",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Product Images",
            },
        ),
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
        migrations.CreateModel(
            name="Vendor",
            fields=[
                (
                    "vid",
                    shortuuid.django_fields.ShortUUIDField(
                        alphabet="abcdefg1234",
                        length=16,
                        max_length=40,
                        prefix="venid_",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("description", models.TextField(blank=True, null=True)),
                ("contact", models.CharField(max_length=100)),
                ("address", models.CharField(max_length=100)),
                ("date", models.DateTimeField(auto_now_add=True, null=True)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "vendors",
            },
        ),
        migrations.AddField(
            model_name="product",
            name="vendor",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="products",
                to="core.vendor",
            ),
        ),
    ]