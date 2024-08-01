from django import template

register = template.Library()

@register.inclusion_tag('includes/menu.html')
def show_menu(menu, info, link_slug):

    return locals()