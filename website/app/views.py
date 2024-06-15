from django.shortcuts import render
from .models import SocialAccounts, Product, ProductType

def base_view(request):
    return render(request, 'main.html')

def company_view(request):
    return render(request, 'company.html')

def solutions_view(request):
    return render(request, 'solutions.html')