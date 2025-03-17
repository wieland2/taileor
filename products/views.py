from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm

def products(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products/products.html', context)

def product(request, pk):
    product = Product.objects.get(id=pk)
    context = {'product': product}
    return render(request, 'products/product.html', context)


def createProduct(request):
    form = ProductForm()

    if request.method == 'POST':
        product = ProductForm(request.POST)
        if product.is_valid():
            product.save()
            return redirect('products')

    context = {'form': form}
    return render(request, 'products/product_form.html', context)


def updateProduct(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products')

    context = {'form': form, 'product': product}
    return render(request, 'products/product_form.html', context)


def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)

    if request.method == 'POST':
        product.delete()
        return redirect('products')

    context = {'product': product}
    return render(request, 'products/delete_form.html', context)
