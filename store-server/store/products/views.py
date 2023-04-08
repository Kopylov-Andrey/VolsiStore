from django.shortcuts import render
from products.models import Product, ProductCategory

# Create your views here.
# контроллеры
def index(request):
    context = {
        'title': 'Volsi',
    }
    return render(request, 'products/index.html', context)

def products(request):
    context = {
        'title': 'Volsi - Каталог',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'products/products.html', context)
