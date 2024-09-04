from django import template

from home.models import MainMenu

register = template.Library()

@register.inclusion_tag('includes/menu.html')
def show_menu(info, main_menu, active_category):

    return locals()

@register.inclusion_tag('includes/footer.html')
def show_footer(info, left, right, services, active_category=0, active_service_category=0):

    return locals()

@register.inclusion_tag('includes/aside.html')
def show_aside(active_about_category=''):
    about_menu = MainMenu.objects.filter(draft=False, is_about_category=True)

    return locals()

@register.filter
def is_first(num):
    if num % 2 != 0:
        return True
    else:
        return False
