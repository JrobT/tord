from website import settings
from django import template
from django.template.defaultfilters import stringfilter

import markdown as md

register = template.Library()


@register.simple_tag
def blogname():
    return settings.blogname

@register.filter()
@stringfilter
def markdown(value):
    return md.markdown(value, extensions=['markdown.extensions.fenced_code'])
