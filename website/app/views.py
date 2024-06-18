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
    
def products(request):
    product_type = request.GET.get('product', 'control_valves')  # Default to control_valves if not specified
    template_name = f'{product_type}.html'  # Construct template name based on the product type
    return render(request, template_name)
