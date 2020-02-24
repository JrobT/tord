import settings
from django import template

register = template.Library()


@register.simple_tag
def blogsite():
    return settings.blogsite