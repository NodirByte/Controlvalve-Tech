from django.contrib import admin
from .models import SocialAccounts, Product, ProductType

admin.site.register(SocialAccounts)
admin.site.register(Product)
admin.site.register(ProductType)
