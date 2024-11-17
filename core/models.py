from django.db import models
from django.utils.html import mark_safe
from shortuuid.django_fields import ShortUUIDField
from userauth.models import User
from django.utils import timezone
from datetime import timedelta


STATUS = (
    ("draft", "Draft"),
    ("disabled", "Disabled"),
    ("rejected", "Rejected"),
    ("in_review", "In Review"),
    ("published", "Published"),
)


# path to the  to the images of the user or profile images
def user_directory_path(instance, filename):
    return "user_{0}/{1}".format(instance.user.id, filename)


############ category model #######################


class Category(models.Model):
    cid = ShortUUIDField(
        length=16,
        max_length=40,
        prefix="catid_",
        alphabet="abcdefg1234",
        primary_key=True,
    )
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="category")

    class Meta:
        verbose_name_plural = "categories"

    def category_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.title


############################## Vendor model ######################################
############################## Vendor model ######################################
############################## Vendor model ######################################


class Vendor(models.Model):
    vid = ShortUUIDField(
        length=16,
        max_length=40,
        prefix="venid_",
        alphabet="abcdefg1234",
        primary_key=True,
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    description = models.TextField(
        null=True, blank=True
    )
    contact = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    is_active = models.BooleanField(default=True)


    class Meta:
        verbose_name_plural = "vendors"

    def __str__(self):
        return self.user.username
    
    def get_time_left(self):
        # Get the current time
        now = timezone.now()

        # Define the free access period (3 months)
        free_access_duration = timedelta(days=90)  # approximately 3 months

        # Calculate the end of the free access period
        free_access_end = self.date + free_access_duration

        # Check how much time is left
        time_left = free_access_end - now

        if time_left.total_seconds() <= 0:
            # If time is up, deactivate the access
            self.is_active = False
            self.save()

            # Return 0 or indicate access is expired
            return 0

        # Return the remaining time in a human-readable format
        return str(time_left.days) + " days"


############################## Product model ######################################
############################## Product model ######################################
############################## Product model ######################################
class Product(models.Model):
    pid = ShortUUIDField(
        length=16,
        max_length=40,
        alphabet="abcdefg1234",
        unique=True,
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, related_name="products"
    )
    vendor = models.ForeignKey(
        Vendor, on_delete=models.SET_NULL, null=True, related_name="products"
    )

    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to=user_directory_path)
    description = models.TextField(
        null=True, blank=True, default="This is the product description"
    )
    price = models.DecimalField( decimal_places=2, default="1.99"
    )
    stock_items = models.IntegerField(null=True, blank=True)

    product_status = models.CharField(
        choices=STATUS, max_length=10, default="in_review"
    )

    status = models.BooleanField(default=True)
    in_stock = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)

    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(null=True, blank=True)


    def product_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.title


class ProductImages(models.Model):
    images = models.ImageField(upload_to="product_images")
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, null=True, related_name="productimages"
    )
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Product Images"

class ProductOfTheWeek(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, null=True, related_name="product"
    )
