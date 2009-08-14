from django.template import Library
register = Library()

@register.filter
def mapformat(floater):
    return "%0.4f" % floater
