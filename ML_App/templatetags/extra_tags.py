from django import template

register = template.Library()

@register.filter
def mod(val, num):
    return val % num