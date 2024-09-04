from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from home.models import Project, MainMenu, Service, Blog, Benefit


class CategorySitemap(Sitemap):
    """Карта категорий сайта"""

    changefreq = 'daily'
    priority = 0.9

    def items(self):
        return MainMenu.objects.filter(draft=False)

class ProjectSitemap(Sitemap):
    """Карта сайта для статей"""

    changefreq = 'weekly'
    priority = 1

    def items(self):
        return Project.objects.filter(draft=False)

    def lastmod(self, obj):
        return obj.time_update

class ServiceSitemap(Sitemap):
    """Карта сайта для сервисов"""

    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Service.objects.filter(draft=False)

    def lastmod(self, obj):
        return obj.time_update

class BlogSitemap(Sitemap):
    """Карта сайта для блогов"""

    changefreq = 'weekly'
    priority = 0.8

    def items(self):
        return Blog.objects.filter(draft=False)

    def lastmod(self, obj):
        return obj.time_update

class BenefitSitemap(Sitemap):
    """Карта сайта для приемуществ"""

    changefreq = 'weekly'
    priority = 0.8

    def items(self):
        return Benefit.objects.filter(draft=False)

    def lastmod(self, obj):
        return obj.time_update