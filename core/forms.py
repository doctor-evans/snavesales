from django import forms
from core.models import Product, ProductImages, Vendor


class AddProductForm(forms.ModelForm):

    title = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Product Title ..."}))
    price = forms.NumberInput()
    description = forms.Textarea(attrs={"placeholder": "Description..."})
    image = forms.ImageField()
    stock_items = forms.IntegerField()

    class Meta:
        model = Product
        fields = ["title", "price", "category", "description", "image", "stock_items"]
        exclude = ["date", "updated", "featured", "product_status", "in_stock"]


class VendorForm(forms.ModelForm):
    description = forms.Textarea(attrs={"placeholder":"Description..."})
    contact = forms.NumberInput(attrs={"placeholder":"2349030xxxxxx"})
    address = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Address..."}))
    class Meta:
        model = Vendor
        fields = ['description', 'contact', 'address']
        exclude = ['is_active', 'date']