from django.shortcuts import render
from .models import SocialAccounts, Product, ProductType
from .services import products, categories

def base_view(request):
    return render(request, 'main.html')

def company_view(request):
    return render(request, 'company.html')

def solutions_view(request):
    return render(request, 'solutions.html')
    
def contact_us_view(request):
    return render(request, 'contact.html')

def category_view(request, id):
    my_products = []
    ids = []
    for i, p in enumerate(products):
        if p['category'] == categories[id]:
            my_products.append(p)
            ids.append(i)

    products_with_ids = list(zip(my_products, ids))

    return render(request, 'category.html', {
        'category': categories[id],
        'products_with_ids': products_with_ids
    })

def product_view(request, id):
    p = products[id]
    return render(request, 'product.html', {'id': id, 'product': p, 'path': p['category'] + ' > ' + p['title']})
