from home.models import MainInfo, MainMenu


def get_info(request):
    info = MainInfo.objects.filter(is_published=True)[0]
    menu = MainMenu.objects.all()
    return locals()