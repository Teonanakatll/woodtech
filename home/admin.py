from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea
from django.utils.safestring import mark_safe

from home.models import MainInfo, MainMenu, Soc, FooterInfo, MainSlide, IndexPage, TrustItem, Project, ProjectPhoto, \
    Benefit, Partner, Blog, Service

formfield_overrides = {
    models.CharField: {'widget': TextInput(attrs={'size': '25'})},
    models.TextField: {'widget': Textarea(attrs={'rows': 5, 'cols': 40})},
}


@admin.register(MainInfo)
class MainInfoAdmin(admin.ModelAdmin):
    """Основная информация о сайте и фирме"""
    list_display = ('big_word', 'thin_word', 'phone', 'address', 'is_published')

    fieldsets = (
        ('Общая информация о сайте и фирме', {
            'fields': (('big_word', 'thin_word', 'phone', 'address'),)
        }),
        ('Категории сайта. Логика маршрутов, get_absolute_url, имён шаблонов и представления завязано на поле url', {
            'fields': (('menu',),)
        }),
        ('Социальные сети', {
            'fields': (('soc',),)
        }),
        ('Текстовые блоки в футере, завязаны на значениях left и right поля side ', {
            'fields': (('footer_info',),)
        })
    )

@admin.register(MainMenu)
class MainMenuAdmin(admin.ModelAdmin):
    """Класс основного меню"""
    list_display = ('name', 'draft', 'is_main_category', 'is_about_category', 'slug', 'header')
    list_editable = ('draft', 'is_main_category', 'is_about_category')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Soc)
class SocAdmin(admin.ModelAdmin):
    """Социальные сети"""
    list_display = ('name', 'draft', 'get_icon', 'link', 'draft')
    list_editable = ('draft',)
    list_editable = ('draft',)
    readonly_fields = ('get_icon',)

    def get_icon(self, object):
        if object.icon:
            return mark_safe(f"<img src='{object.icon.url}' style='background-color: black' height=30 width=30>")

    get_icon.short_description = 'Иконка'

@admin.register(FooterInfo)
class FooterInfoAdmin(admin.ModelAdmin):
    """Текстовые блоки футера"""
    list_display = ('side', 'header')

@admin.register(MainSlide)
class MainSlideAdmin(admin.ModelAdmin):
    """Класс главного слайдера"""
    list_display = ('header', 'draft', 'header_accent', 'get_image')
    list_display_links = ('header', 'header_accent')
    list_editable = ('draft',)
    readonly_fields = ('get_image',)

    def get_image(self, object):
        if object.image:
            return mark_safe(f'<img src="{object.image.url}" height=250 width=auto>')

    get_image.short_description = 'Фото слайда'

class MainSlideInlines(admin.TabularInline):
    """Класс для добавления слайда в классе IndexPage"""
    model = MainSlide
    extra = 1
    readonly_fields = ('get_image',)

    formfield_overrides = formfield_overrides

    def get_image(self, object):
        if object.image:
            return mark_safe(f'<img src="{object.image.url}" height=100 width=auto>')

    get_image.short_description = 'Фото слайда'

@admin.register(TrustItem)
class TrustItemAdmin(admin.ModelAdmin):
    """Информационные блоки секции trust"""
    list_display = ('count', 'string')
    list_display_links = ('count',)

class TrustItemInlines(admin.TabularInline):
    """Для добавления записей через класс IndexPage"""
    model = TrustItem
    extra = 1

@admin.register(ProjectPhoto)
class ProjectPhotoAdmin(admin.ModelAdmin):
    """Фото для отрисовке в слайдере на странице проекта"""
    model = ProjectPhoto
    list_display = ('project', 'get_project_main_image', 'draft', 'get_photo')
    list_editable = ('draft',)
    readonly_fields = ('get_photo', 'get_project_main_image')
    list_filter = ('project', 'draft')

    def get_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' height=100 width=auto>")

    def get_project_main_image(self, object):
        if object.project.main_image:
            return mark_safe(f"<img src='{object.project.main_image.url}' height=100 width=auto>")

    get_photo.short_description = 'Фото проекта'
    get_project_main_image.short_description = 'Главное фото проекта'

class ProjectPhotoInlines(admin.TabularInline):
    """Для добавления фото через класс IndexPage"""
    model = ProjectPhoto
    extra = 3
    readonly_fields = ('get_photo',)

    def get_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' height=100 width=auto>")


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """Информация проекта"""
    list_display = ('name','id', 'draft', 'address', 'get_main_image')
    list_display_links = ('name',)
    readonly_fields = ('get_main_image',)
    list_editable = ('draft',)
    list_filter = ('time_create',)

    prepopulated_fields = {'slug': ('name',)}

    inlines = (ProjectPhotoInlines,)

    def get_main_image(self, object):
        if object.main_image:
            return mark_safe(f'<img src="{object.main_image.url}" height=100 width=auto >')

    get_main_image.short_description = 'Главное фото'

class ProjectInlines(admin.TabularInline):
    """Для длбавления через класс indexPage"""
    model = Project
    extra = 1
    readonly_fields = ('get_main_image',)

    def get_main_image(self, object):
        if object.main_image:
            return mark_safe(f"<img src='{object.main_image.url}' height=100 width=auto>")

    get_main_image.short_description = 'Главное фото'

@admin.register(Benefit)
class BenefitAdmin(admin.ModelAdmin):
    """Информация айтема приемущества"""
    list_display = ('get_icon', 'draft', 'header', 'index_page')
    list_editable = ('draft',)
    list_display_links = ('header',)
    prepopulated_fields = {'slug': ('header',)}

    readonly_fields = ('get_icon',)

    def get_icon(self, object):
        if object.icon:
            return mark_safe(f"<img src='{object.icon.url}' height=70 width=auto>")

    get_icon.short_description = 'Иконка'

class BenefitInlines(admin.TabularInline):
    model = Benefit
    extra = 1
    readonly_fields = ('get_icon',)

    def get_icon(self, object):
        if object.icon:
            return mark_safe(f"<img src='{object.icon.url}' height=70 width=auto>")

    get_icon.short_description = 'Иконка'

@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    """Информация айтема секции partners"""
    list_display = ('get_label', 'draft', 'name', 'short')
    list_display_links = ('name',)
    list_editable = ('draft',)
    readonly_fields = ('get_label',)

    def get_label(self, object):
        if object.label:
            return mark_safe(f"<img src='{object.label.url}' style='background-color:black' height=70 width=auto>")

    get_label.short_description = 'Лейбл фирмы'

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    """Информация айтема секции blog"""
    list_display = ('header','draft', 'get_main_image', 'index_page')
    list_display_links = ('header',)
    list_editable = ('draft',)
    readonly_fields = ('get_main_image',)
    prepopulated_fields = {'slug': ('header',)}

    def get_main_image(self, object):
        if object.main_image:
            return mark_safe(f"<img src='{object.main_image.url}' height=100 width=auto>")

    get_main_image.short_description = 'Главное фото блога'

class BlogInlines(admin.TabularInline):
    model = Blog
    extra = 1
    readonly_fields = ('get_main_image',)

    def get_main_image(self, object):
        if object.main_image:
            return mark_safe(f"<img src='{object.main_image.url}' height=100 width=auto>")

    get_main_image.short_description = 'Главное фото блога'

@admin.register(IndexPage)
class IndexPageAdmin(admin.ModelAdmin):
    """Информация секций главной страницы"""
    list_display = ('sect_trust_header', 'sect_trust_text', 'get_sect_about_image')
    list_display_links = ('sect_trust_header',)

    inlines = [MainSlideInlines, TrustItemInlines, ProjectInlines, BenefitInlines, BlogInlines]
    readonly_fields = ('get_sect_about_image',)

    def get_sect_about_image(self, object):
        if object.sect_about_image:
            return mark_safe(f"<img src='{object.sect_about_image.url}' height=100 width=auto>")

    get_sect_about_image.short_description = 'Фото секции about'


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    """Информация айтема сервиса"""
    list_display = ('header', 'draft', 'get_image')
    list_editable = ('draft',)
    readonly_fields = ('get_image',)

    prepopulated_fields = {'slug': ('header',)}

    def get_image(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' height=100 width=auto")

    get_image.short_description = 'Фото сервиса'

admin.site.site_title = 'Админ-панель сайта Woodthech'
admin.site.site_header = 'Админ-панель сайта Woodthech'
