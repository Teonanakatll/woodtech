from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404

from home.models import IndexPage, Partner, Project, MainMenu, Blog, Benefit, Service
from home.utils import get_list


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
    project = Project.objects.filter(slug=slug).prefetch_related('projectphoto_set')[0]
    slides = project.projectphoto_set.filter(draft=False)

    # если в проекте нет связанных слайдов
    if not project.projectphoto_set.exists():
        proj = Project.objects.prefetch_related('projectphoto_set')[0]
        slides = proj.projectphoto_set.filter(draft=False)


    return render(request, 'project.html', locals())

# def benefit(request):

def benefit_article(request, slug):
    article = get_object_or_404(Benefit, slug=slug)

    return render(request, 'universal_page.html', locals())

def partners(request):
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
    return render(request, f'{slug}.html', locals())
