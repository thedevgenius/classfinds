from django import template
from datetime import datetime

register = template.Library()

@register.simple_tag
def multiply(a, b):
    return a * b

@register.filter
def exp_number(value):
    current_year = datetime.now().year
    experience = current_year - value
    return experience

@register.simple_tag
def whatsapp_url(phone):
    message = f"Hello, I found your profile on Classfinds. I am looking for a home tutor. Are you available?"
    from urllib.parse import quote
    return f"https://wa.me/{phone}?text={quote(message)}"