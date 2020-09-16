from django import template

register = template.Library()

@register.filter
def my_add(v1, v2):
    return v1 + v2


@register.filter
def my_str(v1, v2):
    return v1+v2


@register.filter
def get_num(v1, v2):
    return v1%v2 == 0


@register.simple_tag
def get_str(v1, v2, v3):
    return v1+'['+v2+']'+v3


@register.simple_tag
def get_max(v1, v2, v3):
    return  max(v1, v2, v3)

