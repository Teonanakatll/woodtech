from home.models import MainInfo, MainMenu, Service


def get_info(request):
    info = MainInfo.objects.prefetch_related('menu', 'soc', 'footer_info').get(id=1)
    main_menu = info.menu.filter(draft=False, is_main_category=True)
    all = info.footer_info.all()
    right = all[1]
    left = all[0]
    services = Service.objects.filter(draft=False)

    return locals()