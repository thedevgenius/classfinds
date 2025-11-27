from django import template
from datetime import datetime
from business.models import Location

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

@register.filter
def get_location(value):
    location = Location.objects.get(id=value)
    if location:
        return location.name
    return "Kolkata"