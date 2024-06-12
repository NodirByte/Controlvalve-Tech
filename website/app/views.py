from django.shortcuts import render
from .models import SocialAccounts, Product, ProductType

def base_view(request):
    social_accounts = SocialAccounts.objects.first()
    products = Product.objects.all()
    product_types = ProductType.objects.all()
    return render(request, 'layout/base.html', {
        'social_accounts': social_accounts,
        'products': products,
        'product_types': product_types,
   })

def company_view(request):
    return render(request, 'company.html')