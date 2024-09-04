from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Prefetch
from django.shortcuts import render, get_object_or_404

from home.models import IndexPage, Partner, Project, MainMenu, Blog, Benefit, Service, ProjectPhoto, ProjectWorker, \
    ProjectCharacteristic
from home.utils import get_list

from django.views.decorators.cache import cache_page
from datetime import timedelta

# @cache_page(60*5)
def index(request):
    active_category = 'index'
    index_info = IndexPage.objects.prefetch_related('mainslide_set', 'trustitem_set', 'project_set', 'benefit_set', 'blog_set')[0]
    slides = index_info.mainslide_set.filter(draft=False)
    projects = index_info.project_set.filter(draft=False)[:3]
    benefits = index_info.benefit_set.filter(draft=False)[:2]
    blogs = index_info.blog_set.filter(draft=False)[:2]
    partners = Partner.objects.filter(draft=False)

    return render(request, 'index.html', locals())

def projects(request, slug):
    active_category = slug
    proj = Project.objects.filter(draft=False)
    page_info = get_object_or_404(MainMenu, slug=slug)

    # функция get_list в utils разбивает список записей на списки для отрисовки (sect1, sect2)
    lst = get_list(proj)

    return render(request, f'{slug}.html', locals())

def project_article(request, slug):
    all = Project.objects.prefetch_related('projectphoto_set', 'project_chars',
                            Prefetch('project_workers', queryset=ProjectWorker.objects.all()))
    project = all.filter(slug=slug)[0]


    # если существуют связанные с проектом фото для слайдера
    if project.projectphoto_set.exists():
        slides = project.projectphoto_set.filter(draft=False)
    else:
        # иначе для отрисовки на странице берём слайды первого проекта

        slides = ProjectPhoto.objects.filter(draft=False)[:9]

    # если существует связанный с проектом работник
    if project.project_workers.exists():
        worker = project.project_workers.all()[0]
    else:

        worker = ProjectWorker.objects.all()[0]

    if project.project_chars.exists():
        chars = project.project_chars.all()
    else:
        chars = ProjectCharacteristic.objects.all()[:5]



    return render(request, 'project.html', locals())

def benefits(request, slug):
    active_about_category = slug
    page_info = get_object_or_404(MainMenu, slug=slug)
    benefits = Benefit.objects.filter(draft=False)

    return render(request, 'benefits.html', locals())


def benefit_article(request, slug):
    article = get_object_or_404(Benefit, slug=slug)

    return render(request, 'universal_page.html', locals())

def partners(request, slug):
    active_about_category = slug
    page_info = get_object_or_404(MainMenu, slug=slug)
    partners = Partner.objects.filter(draft=False)

    return render(request, 'partners.html', locals())

def services(request, slug):
    active_category = slug
    page_info = get_object_or_404(MainMenu, slug=slug)
    services = Service.objects.filter(draft=False)

    return render(request, f'{slug}.html', locals())

def service_article(request, slug):
    article = get_object_or_404(Service, slug=slug)
    active_service_category = article.slug

    return render(request, 'universal_page.html', locals())

def blog(request, slug):
    active_category = slug
    page_info = get_object_or_404(MainMenu, slug=slug)
    blogs = Blog.objects.filter(draft=False)

    paginator = Paginator(blogs, 6)
    # print('PAGINATOR', paginator.num_pages)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)
    # если указанная страница не является целым числом
    except PageNotAnInteger:
        page_obj = paginator.get_page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    return render(request, f'{slug}.html', locals())

def blog_article(request, slug):
    article = get_object_or_404(Blog, slug=slug)

    return render(request, 'universal_page.html', locals())

def company(request, slug):
    active_category = slug
    active_about_category = slug
    page_info = get_object_or_404(MainMenu, slug=slug)

    return render(request, f'{slug}.html', locals())

def feedback(request, slug):
    active_about_category = slug

    return render(request, f'{slug}.html', locals())
