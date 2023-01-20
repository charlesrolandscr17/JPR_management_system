from django import template
import random


register = template.Library()
        
@register.filter
def bgcolor(i):
    if i > 4:
        i = i%5
        
    return  ["table-secondary","table-danger","table-warning","table-success","table-info"][i]



@register.filter
def typeOf(value):
    return type(value)
