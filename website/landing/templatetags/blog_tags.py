from django import template
from website import settings

register = template.Library()


@register.simple_tag
def blogname():
    return settings.blogname
