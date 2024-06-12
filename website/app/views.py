from django.shortcuts import render
from .models import SocialAccounts, Product, ProductType

def base(request):
    social_accounts = SocialAccounts.objects.first()
    products = Product.objects.all()
    product_types = ProductType.objects.all()
    return render(request, 'base.html', {
        'social_accounts': social_accounts,
        'products': products,
        'product_types': product_types,
   })