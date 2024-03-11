from django import template

register = template.Library()


@register.filter
def filter_tag(things, filter_dict):
    return things.filter(**filter_dict)
