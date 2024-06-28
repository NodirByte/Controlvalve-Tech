from django import template

register = template.Library()

@register.filter(name='replace')
def replace(value, arg1, arg2):
    return value.replace(arg1, arg2)
