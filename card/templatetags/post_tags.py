from atexit import register
from django import template
from ..models import invcard

register=template.Library()

@register.simple_tag

def alcard():
    allcart= []
    cats= invcard.objects.values('category', 'code')
    cat= {item['category'] for item in cats}
    for i in cat:
        cards= invcard.objects.filter(category= i)
        allcart.append(cards)

    return allcart