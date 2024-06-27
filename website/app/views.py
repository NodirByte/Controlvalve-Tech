from django.shortcuts import render, redirect
from .models import SocialAccounts, Product, ProductType
from .services import products, categories
from django.http import HttpResponse
from django.contrib import messages
import requests

BOT_TOKEN = '7273119160:AAGbaipGb4Q_myfZo1GoLe48aKktB08Y4tw'
ADMIN_IDs = ['1180612659', '2367366']

def base_view(request, lan):
    return render(request, 'main.html', {'language': lan})

def company_view(request, lan):
    return render(request, 'company.html', {'language': lan})

def solutions_view(request, lan):
    return render(request, 'solutions.html', {'language': lan})

def contact_us_view(request, lan):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        special_note = request.POST.get('special_note')
        
        data = f'<b>Wenzhou Feihang Flow Control Co., Ltd</b>\n<b>📋 Name:</b> {name}\n<b>📧 Email:</b> {email}\n<b>📞 Phone:</b> {phone_number}\n<b>✉️ Message:</b> {special_note}\n\nfeihangflow.com'
        url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
        for id in ADMIN_IDs:
            requests.post(url, data={'chat_id': id, 'text': data, 'parse_mode': 'HTML'})
        
        # Add a success message
        messages.success(request, 'Форма успешно отправлена!')

        return redirect('contact_us', lan=lan)

    return render(request, 'contact.html', {'language': lan})

def category_view(request, id, lan):
    my_products = []
    ids = []
    for i, p in enumerate(products):
        if p['category'] == categories[id]:
            my_products.append(p)
            ids.append(i)

    products_with_ids = list(zip(my_products, ids))

    return render(request, 'category.html', {
        'category': categories[id],
        'products_with_ids': products_with_ids,
        'language': lan
    })

def product_view(request, id, lan):
    p = products[id]
    return render(request, 'product.html', {
        'id': id, 
        'product': p, 
        'path': p['category'] + ' > ' + p['title'],
        'language': lan
    })
