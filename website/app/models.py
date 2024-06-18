from django.db import models
from django.utils.translation import gettext_lazy as _

class SocialAccounts(models.Model):
    telegram = models.URLField(_('Telegram'), default='https://t.me/Nodirbyte')
    facebook = models.URLField(_('Facebook'), default='https://www.facebook.com/nodirbyte', blank=True, null=True)
    instagram = models.URLField(_('Instagram'), default='https://www.instagram.com/nodirbyte', blank=True, null=True)
    wechat = models.URLField(_('WeChat'), default='https://www.wechat.com/nodirbyte', blank=True, null=True)
    whatsapp = models.URLField(_('WhatsApp'), default='https://www.whatsapp.com/nodirbyte', blank=True, null=True)
    email = models.EmailField(_('Email'), default='nodirbyte@gmail.com', blank=True, null=True)
    phone = models.CharField(_('Phone'), max_length=15, default='+998 99 785 48 02', blank=True, null=True)
    location = models.CharField(_('Location'), max_length=255, default='Tashkent, Uzbekistan', blank=True, null=True)
    location_map = models.URLField(_('Location Map'), default='https://goo.gl/maps/1JZzZQ1Zz1Z1Zz1Z1', blank=True, null=True)
    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated At'), auto_now=True)
    
    class Meta:
        verbose_name = _('Social Account')
        verbose_name_plural = _('Social Accounts')

class Product(models.Model):
    title = models.CharField(_('Title'), max_length=255)
    description = models.TextField(_('Description'))
    image = models.ImageField(_('Image'), upload_to='products')
    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated At'), auto_now=True)
    
    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
        
class ProductType(models.Model):
    title = models.CharField(_('Title'), max_length=255)
    products = models.ManyToManyField(Product, related_name='product_types')
    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated At'), auto_now=True)
    
    class Meta:
        verbose_name = _('Product Type')
        verbose_name_plural = _('Product Types')

