from django import template

register = template.library()


def myfilter(value):
    return value + "This is from filter"


register.filter('custom_filter', myfilter)
