from django.shortcuts import render
from .models import SocialAccounts, Product, ProductType

def base_view(request):
    return render(request, 'main.html')

def company_view(request):
    return render(request, 'company.html')

def solutions_view(request):
    return render(request, 'solutions.html')
    
def contact_us_view(request):
    return render(request, 'contact.html')
    
products = [
    {
        'title': 'Product',
        'description': 'Product description',
        'image': 'images/product.jpg',
    },
    {
        'title': 'Product2',
        'description': 'Product2 description',
        'image': 'images/product.jpg',
    }
]
    
def category_view(request, id):
    return render(request, 'category.html', {'id': id, 'category': 'Control values', 'products': products})

def product_view(request, id):
    return render(request, 'product.html')
