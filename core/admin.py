from django.contrib import admin



# Register your models here.
from core.models import (
    Product,
    ProductImages,
    Category,
    Vendor,
    ProductOfTheWeek
)


class ProductImageAdmin(admin.TabularInline):
    model = ProductImages


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin]
    list_display = [
        "user",
        "title",
        "product_image",
        "price",
        "category",
        "vendor",
        "featured",
        "product_status",
        "in_stock"
    ]
    list_editable = ["featured", "product_status", "in_stock"]




class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "category_image"]


class VendorAdmin(admin.ModelAdmin):
    list_display = ["user", 'is_active', 'time_left']
    def time_left(self, obj):
        return obj.get_time_left()
    
    # Make this method read-only in the form view
    time_left.short_description = 'Time Left'

    # If you want it to show up in the form as well, you can add it to the fields or readonly_fields
    readonly_fields = ('time_left',)

class ProductOfTheWeekAdmin(admin.ModelAdmin):
    list_display = ["product"]


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Vendor, VendorAdmin)
admin.site.register(ProductOfTheWeek, ProductOfTheWeekAdmin)

