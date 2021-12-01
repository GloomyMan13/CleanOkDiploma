from home.models import Footer, Footerr

from django import template
from ..map.map import write_code

register = template.Library()


@register.inclusion_tag('home/tags/footer.html', takes_context=True)
def footer_tag(context):
    write_code()
    return {
        'request': context['request'],
        'footerr': Footerr.objects.first(),
        'footerl': Footer.objects.first()
    }
