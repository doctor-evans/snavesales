from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from core.forms import AddProductForm, VendorForm
from core.models import Product, ProductImages, Vendor, Category, ProductOfTheWeek
from userauth.models import User
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required




# Create your views here.
def index(request):
    featured_products = Product.objects.filter(product_status="published", featured=True).order_by('-date')
    product_of_the_week = ProductOfTheWeek.objects.last()
    context = {
        "featured_products": featured_products,
        "product_of_the_week": product_of_the_week,
    }
    return render(request, 'core/index.html', context)


def store(request):
    products = Product.objects.filter(product_status="published").order_by('-date')
    context = {
        "products":products
    }
    return render(request, "core/store.html", context)


def product_detail(request, pid):
    product = Product.objects.get(pid=pid)
    product_images = product.productimages.all()
    context = {
        "product":product,
        "product_images":product_images,
    }
    return render(request, "core/product_detail.html", context)

def searchView(request):
    query = request.GET["search_query"]
    products = Product.objects.filter(title__icontains=query).order_by("-date")

    context = {
        "products": products,
        "query": query,
    }
    return render(request, "core/search.html", context)


def sellview(request):
    return render(request, "core/sell.html")

@login_required(login_url=("userauth:login"))
def accountView(request):
    products = Product.objects.filter(user = request.user)
    try:
        vendor = Vendor.objects.get(user = request.user)
    except:
        vendor = ''
    context = {
        "products":products,
        "vendor":vendor
    }
    return render(request, "core/dashboard.html", context)

# @login_required(login_url=("userauth:login"))
# def vendorUpdate(request):
#     user_id = request.GET.get('user_id')

#     index_user = get_object_or_404(User, id=user_id)
    
#     title = index_user.username
#     contact = request.GET.get('contact')
#     address = request.GET.get('address')
#     description = request.GET.get('description')

#     try:
#         vendor = Vendor.objects.get(user = index_user)
#         # Update user fields
#         vendor.user = index_user
#         vendor.title = title
#         vendor.contact = contact
#         vendor.address = address
#         vendor.description = description
#         if vendor.get_time_left > 0:
#             vendor.is_active = True
#         else:
#             vendor.is_active = False
#         vendor.save()
#     except:
#         vendor = Vendor.objects.create(
#             user = index_user,
#             title = title,
#             contact = contact,
#             address = address,
#             description = description,
#             is_active = True
#         )


#     context = render_to_string("userauth/async/vendor-update.html", {
#         'user': index_user,
#         'vendor': vendor
#         })

#     return JsonResponse({'bool':True, 'data': context})


@login_required(login_url=("userauth:login"))
def addnewProduct(request):
    if request.method == 'POST':
        vendor = Vendor.objects.get(user = request.user)
        
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.vendor = vendor
            product.save()  # Save the product to the database
            return redirect("core:dashboard")
        else:
            print(form.errors)
    else:
        form = AddProductForm()
    context = {
        'form':form
    }
    return render(request, 'core/newproduct.html', context)


@login_required(login_url=("userauth:login"))
def updateProductView(request, pid):
    product = Product.objects.get(pid = pid)
    if request.method == 'POST':
        vendor = Vendor.objects.get(user = request.user)
        
        form = AddProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.vendor = vendor
            product.save()  # Save the product to the database
            return redirect("core:dashboard")
        else:
            print(form.errors)
    else:
        form = AddProductForm(instance=product)
    context = {
        'form':form,
        'product':product
    }
    return render(request, 'core/updateproduct.html', context)

@login_required(login_url=("userauth:login"))
def deleteProduct(request, pid):
    product = Product.objects.get(pid=pid)
    product.delete()
    return redirect("core:dashboard")


@login_required(login_url=("userauth:login"))
def updateVendor(request):
    if request.method == 'POST':
        try:
            vendor = Vendor.objects.get(user=request.user)
            
            form = VendorForm(request.POST, instance=vendor)
            if form.is_valid():
                vendor_form = form.save(commit=False)
                vendor_form.user = request.user
                vendor_form.save()
                return redirect("core:dashboard")
        except:
            form = VendorForm(request.POST)
            if form.is_valid():
                vendor_form = form.save(commit=False)
                vendor_form.user = request.user
                vendor_form.save()
                return redirect("core:dashboard")
    else:
        form = VendorForm()
    
    context = {
        'form':form
    }

    return render(request, 'core/update_vendor.html', context)