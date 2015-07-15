from django import template

register = template.Library()

@register.filter(name='lookup')
def lookup(d, key):
    if key not in d:
        return None
    return d[key]

@register.filter(name='is_filled')
def is_filled(obj, country):
    return obj.is_filled(country)