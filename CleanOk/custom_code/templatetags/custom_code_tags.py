from django import template

from ..models import CustomCode

register = template.Library()


@register.simple_tag()
def get_code(slug):
    return CustomCode.objects.get(slug=slug)

# @register.simple_tag()
# def get_codes():
#     return CustomCode.objects.all()