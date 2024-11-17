from django.urls import path
from core import views

app_name = "core"

urlpatterns = [
    path("", views.index, name="index"),
    path("store/", views.store, name = "store"),
    path("store/product/<pid>", views.product_detail, name="product_detail"),
    path("search/", views.searchView, name="search_view"),
    path("sell-guide/", views.sellview, name="sell_guide"),
    path("dashboard/", views.accountView, name="dashboard"),
    # path("vendor-update/", views.vendorUpdate, name="vendor-update"),
    path("add-new-product/", views.addnewProduct, name='addnewproduct'),
    path("update-product/<pid>", views.updateProductView, name="updateproduct"),
    path("delete-product/<pid>", views.deleteProduct, name="deleteproduct"),
    path("vendor", views.updateVendor, name="updatevendor"),
]
