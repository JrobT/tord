from website import settings
from django import template

register = template.Library()


@register.simple_tag
def blogname():
    return settings.blogname
