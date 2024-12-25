from django.shortcuts import render, redirect
from .models import SocialAccounts, Product, ProductType
from .services import products, categories, products_en, categories_en
from django.http import HttpResponse, Http404
from django.contrib import messages
import requests
from django.http import HttpResponseBadRequest
from django_ratelimit.decorators import ratelimit

BOT_TOKEN = '7273119160:AAEzNfEopkUkmiuCKI8uMkiObu1xNEjvYsE'
ADMIN_IDs = ['1180612659', '2367366']

def validate_language(lan):
    if lan not in ['en', 'ru']:
        raise Http404("Language not supported")

def pre_base_view(request):
    return redirect('base', lan='ru')

def base_view(request, lan):
    validate_language(lan)
    current_url = request.get_full_path()[:-3]  # Get current URL path without last 3 characters
    return render(request, 'main.html', {'language': lan, 'current_url': current_url})

def company_view(request, lan):
    validate_language(lan)
    current_url = request.get_full_path()[:-3]  # Get current URL path without last 3 characters
    return render(request, 'company.html', {'language': lan, 'current_url': current_url})

def solutions_view(request, lan):
    validate_language(lan)
    current_url = request.get_full_path()[:-3]  # Get current URL path without last 3 characters
    return render(request, 'solutions.html', {'language': lan, 'current_url': current_url})

@ratelimit(key='ip', rate='2/m', block=True)  # 5 requests per minute per IP
def contact_us_view(request, lan):
    if request.method == 'POST':
        # Honeypot validation
        honeypot = request.POST.get('honeypot', '')
        if honeypot:
            return HttpResponseBadRequest("Bot detected!")

        # Retrieve form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        special_note = request.POST.get('special_note')

        # Basic filtering for spam
        if name.lower() in ['blockedname', 'spam', 'bot']:
            return HttpResponseBadRequest("Suspicious activity detected!")

        # Send data to Telegram
        data = f'<b>Wenzhou Feihang Flow Control Co., Ltd</b>\n<b>📋 Name:</b> {name}\n<b>📧 Email:</b> {email}\n<b>📞 Phone:</b> {phone_number}\n<b>✉️ Message:</b> {special_note}\n\nfeihangflow.com'
        url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
        for id in ADMIN_IDs:  
            response = requests.post(url, data={'chat_id': id, 'text': data, 'parse_mode': 'HTML'})

        # Show success message and redirect
        messages.success(request, 'Your form was submitted successfully!')
        return redirect('contact_us', lan=lan)

    # Render the contact form
    return render(request, 'contact.html', {'language': lan})

def category_view(request, id, lan):
    validate_language(lan)
    my_products = []
    ids = []
    language = request.get_full_path()[-3:]
    if 'en/' == language : 
        ctg = categories_en 
        prod = products_en
    else: 
        ctg = categories
        prod = products

    for i, p in enumerate(prod):
        if p['category'] == ctg[id]:
            my_products.append(p)
            ids.append(i)

    products_with_ids = list(zip(my_products, ids))

    current_url = request.get_full_path()[:-3]  # Get current URL path without last 3 characters
    return render(request, 'category.html', {
        'category': ctg[id],
        'products_with_ids': products_with_ids,
        'language': lan,
        'current_url': current_url
    })

def product_view(request, id, lan):
    validate_language(lan)
    language = request.get_full_path()[-3:]
    if 'en/' == language : 
        prod = products_en
    else: 
        prod = products

    p = prod[id]
    current_url = request.get_full_path()[:-3]  # Get current URL path without last 3 characters
    return render(request, 'product.html', {
        'id': id, 
        'product': p, 
        'path': p['category'] + ' > ' + p['title'],
        'language': lan,
        'current_url': current_url
    })
