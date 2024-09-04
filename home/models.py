from datetime import datetime

from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.db import models
from django.urls import reverse

from django_ckeditor_5.fields import CKEditor5Field


class MainMenu(models.Model):
    """Основное меню"""
    name = models.CharField('Название пункта меню', max_length=25)
    header = models.CharField('Заголовок страницы', max_length=60, blank=True)
    description = models.TextField('Описание', blank=True)
    article = CKEditor5Field('Статья', config_name='extends', null=True, default=None, blank=True)
    slug = models.SlugField('url', max_length=50, unique=True, db_index=True, default='')
    draft = models.BooleanField('Черновик', default=True)
    is_main_category = models.BooleanField('Пункт главного меню', default=True)
    is_about_category = models.BooleanField('Пункт меню о компании', default=False)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        if self.slug == 'index':
            return reverse('home:index')

        return reverse(f'home:{self.slug}', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Категория главного меню и меню about'
        verbose_name_plural = 'Категории главного меню и меню about'


class Soc(models.Model):
    """Социальные сети"""
    name = models.CharField('Имя', max_length=50)
    icon = models.FileField('Иконка', blank=True, upload_to='images/soc_icons', validators=[FileExtensionValidator(['svg', ])])
    link = models.URLField('Ссылка', max_length=150, blank=True)
    draft = models.BooleanField('Черновик', default=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Аккаунт в социальной сети'
        verbose_name_plural = 'Аккаунты в социальных сетях'


class FooterInfo(models.Model):
    """Текстовые блоки в футере слева и справа завязанны на значениях left и right поля side"""
    # сторона с которай будет отрисовываться информация
    side = models.CharField('Сторона', max_length=10, blank=True)
    header = models.CharField('Заголовок', max_length=25, blank=True)
    description = models.TextField('Описание', blank=True)

    def __str__(self):
        return self.header

    class Meta:
        verbose_name = 'Информация футера'
        verbose_name_plural = 'Информация футера'


class MainInfo(models.Model):
    """ Основная информация о сайте, название, телефон и адресс"""
    big_word = models.CharField('Первое слово названия', max_length=30, blank=True)
    thin_word = models.CharField('Второе слово', max_length=30, blank=True)
    feedback_header = models.CharField('Заголовок обратной связи', max_length=100, default='', blank=True)
    feedback_short = models.CharField('Описание обратной связи', max_length=255, default='', blank=True)
    phone = models.CharField('Телефон', max_length=25, blank=True)
    address = models.CharField('Адрес', max_length=150, blank=True)
    map = models.TextField('Ссылка на карту', blank=True, null=True, default=0)
    is_published = models.BooleanField('Опубликовать', default=False, blank=True)
    menu = models.ManyToManyField(MainMenu, related_name='main_menu', blank=True)
    soc = models.ManyToManyField(Soc, related_name='site_soc', blank=True)
    footer_info = models.ManyToManyField(FooterInfo, blank=True)

    def __str__(self):
        return f'{self.big_word} {self.thin_word}'

    class Meta:
        verbose_name = 'Название сайта и контакты'
        verbose_name_plural = 'Название сайта и контакты'




#                                     index.html


class IndexPage(models.Model):
    """Моделя для хранения данных секций страницы index.html"""
    sect_trust_header = models.CharField('Заголовок секции trust', max_length=40, blank=True)
    sect_trust_text = models.CharField('Текстовая инФ. секции trust', max_length=255, default='', blank=True)

    sect_projects_accent = models.CharField('Заголовок акцентный секции projects', max_length=40, default='', blank=True)
    sect_projects_header = models.CharField('Заголовок секции projects', max_length=80, default='', blank=True)
    sect_projects_text = models.TextField('Текст секции projects', default='', blank=True)

    sect_about_accent = models.CharField('Заголовок акцентный секции about', max_length=40, default='', blank=True)
    sect_about_header = models.CharField('Заголовок секции about', max_length=80, default='', blank=True)
    sect_about_text = models.TextField('Текст секции about', default='', blank=True)
    sect_about_frame_number = models.PositiveSmallIntegerField('Цифра в рамке', blank=True, null=True, default=0)
    sect_about_frame_string = models.CharField('Текст в рамке', max_length=30, default=None, blank=True, null=True)
    sect_about_image = models.ImageField('Изображение секции about', upload_to='images/about/', default=None, blank=True, null=True)

    sect_partners_header = models.CharField('Заголовок секции partners', max_length=50, blank=True, default='')
    sect_partners_background = models.ImageField('Фото фона секции partners', upload_to='images/backgroud/', blank=True, null=True, default=None)

    sect_blog_header = models.CharField('Заголовок секции blog', max_length=100, null=True, default=None, blank=True)
    sect_blog_background_more = models.ImageField('Фон ссылки на все записи', upload_to='images/background/', null=True, default=None, blank=True)

    def __str__(self):
        return f'{self.sect_trust_header} - {self.sect_trust_text}'

    class Meta:
        verbose_name = 'ДАННЫЕ ГЛАВНОЙ СТРАНИЦЫ'
        verbose_name_plural = 'ДАННЫЕ ГЛАВНОЙ СТРАНИЦЫ'


class MainSlide(models.Model):
    """Модели слайдов главной страницы"""
    image = models.ImageField('Изображение', upload_to='images/main_slide')
    header = models.CharField('Заголовок', max_length=35)
    header_accent = models.CharField('Выделенный заголовок', max_length=120)
    text = models.TextField('Текст')
    index_page = models.ForeignKey(IndexPage, on_delete=models.DO_NOTHING, blank=True, null=True, default=None)
    draft = models.BooleanField('Черновик', default=True)

    def __str__(self):
        return self.header

    class Meta:
        verbose_name = 'Слайд главной страницы'
        verbose_name_plural = 'Слайды главной страницы'


class TrustItem(models.Model):
    """Информация в секции траст"""
    count = models.PositiveSmallIntegerField('Количество', null=True, blank=True)
    string = models.CharField('Описание', max_length=150, blank=True)
    index_page = models.ForeignKey(IndexPage, on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return f'{self.count} - {self.string}'

    class Meta:
        verbose_name = 'Айтем секции trast'
        verbose_name_plural = 'Айтем секции trast'





class Project(models.Model):
    """Информация страницы проекта    project.html"""
    main_image = models.ImageField('Главное изображение', upload_to='images/projects/%Y/%m/%d/', blank=True)
    name = models.CharField('Заголовок', max_length=255, blank=True)
    slug = models.SlugField('Url', null=True, default=None, unique=True, db_index=True)
    address = models.CharField('Адрес', max_length=255, blank=True)
    client = models.CharField('Заказчик', max_length=150, blank=True, default='')
    article = CKEditor5Field('Статья', config_name='extends', default=None, blank=True)
    time_create = models.DateTimeField('Время создания', auto_now_add=True)
    time_update = models.DateTimeField('Время изменения', auto_now=True)
    index_page = models.ForeignKey(IndexPage, on_delete=models.PROTECT, blank=True, null=True)
    draft = models.BooleanField('Черновик', default=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home:project', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
        ordering = ['id']


class ProjectCharacteristic(models.Model):
    """Класс описывающий характеристики проекта"""
    name = models.CharField('Название характеристики проекта', max_length=20, blank=True)
    number = models.CharField('Числовое значение характеристики', max_length=5, blank=True)
    words = models.CharField('Опсание в 1-2 словах: метров, лет и тд', max_length=20, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, default=None, related_name='project_chars')

    def __str__(self):
        return f'{self.name} - {self.number} {self.words}'

    class Meta:
        verbose_name = 'Характеристика проекта'
        verbose_name_plural = 'Характеристики проекта'


class ProjectPhoto(models.Model):
    """Фото проекта"""
    photo = models.ImageField('Фото проекта для слайдера', upload_to='images/projects/%Y/%m/%d/')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, default=None, blank=True)
    draft = models.BooleanField('Черновик', default=True)

    class Meta:
        verbose_name = 'Фото проекта'
        verbose_name_plural = 'Фото проекта'
        ordering = ['id']


class ProjectWorker(models.Model):
    """Класс описывает архитектора или дизайнера проекта"""
    photo = models.ImageField('Фото работника', upload_to='image/workers/', blank=True)
    profession = models.CharField('Профессия', max_length=100, blank=True)
    name = models.CharField('Имя', max_length=70, blank=True)
    description = models.TextField('Описание', blank=True)
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING, blank=True, related_name='project_workers')

    def __str__(self):
        return f'{self.profession} - {self.name}'

    class Meta:
        verbose_name = 'Работник проекта'
        verbose_name_plural = 'Работники проекта'




class Benefit(models.Model):
    """Класс описывающий айтем приемущества"""
    icon = models.FileField('Иконка', blank=True, upload_to='images/benefit_icons', validators=[FileExtensionValidator(['svg', ])])
    header = models.CharField('Заголовок', max_length=50, default='', blank=True)
    slug = models.SlugField('url', unique=True, db_index=True, null=True, default=None)
    short = models.CharField('Короткое описание', max_length=255, blank=True)
    article = CKEditor5Field('Статья', config_name='extends', blank=True)
    index_page = models.ForeignKey(IndexPage, on_delete=models.DO_NOTHING, blank=True, null=True, default=None)
    draft = models.BooleanField('Черновик', default=True)
    time_update = models.DateTimeField('Дата изменения', auto_now=True)


    def __str__(self):
        return self.header

    def get_absolute_url(self):
        return reverse('home:benefit', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Приемущество'
        verbose_name_plural = 'Приемущества'


class Partner(models.Model):
    """Класс описывающий айтем партнёра"""
    label = models.ImageField('Лейбл фирмы', upload_to='images/partners/', blank=True)
    name = models.CharField('Название фирмы', max_length=100, blank=True)
    short = models.CharField('Краткое описание фирмы', max_length=170, blank=True)
    text = models.TextField('Описание фирмы', null=True, default=None, blank=True)
    article = CKEditor5Field('Описание фирмы', config_name='extends', blank=True)
    draft = models.BooleanField('Черновик', default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Фирма партнёр'
        verbose_name_plural = 'Фирмы партнёры'


class Blog(models.Model):
    """Информация айтема секции блог"""
    main_image = models.ImageField('Главное фото айтема blog', upload_to='images/blog/', blank=True)
    header = models.CharField('Название', max_length=100, blank=True)
    slug = models.SlugField('url', unique=True, db_index=True, null=True, default=None)
    short = models.CharField('Краткое описание', max_length=250, blank=True)
    day = models.PositiveSmallIntegerField('Число', blank=True)
    month = models.CharField('Месяц', max_length=15, blank=True)
    time_update = models.DateTimeField('Дата изменения', auto_now=True)
    index_page = models.ForeignKey(IndexPage, on_delete=models.DO_NOTHING, null=True, default=None, blank=True)
    article = CKEditor5Field('Статья', config_name='extends', blank=True)
    draft = models.BooleanField('Черновик', default=True)

    def __str__(self):
        return self.header

    def get_absolute_url(self):
        return reverse('home:article', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Статья блога'
        verbose_name_plural = 'Статьи блога'
        ordering = ('id',)


class Service(models.Model):
    """Класс описывающий айтем сервиса"""
    header = models.CharField('Заголовок', max_length=100, blank=True)
    short = models.CharField('Краткое описание', max_length=255, blank=True)
    draft = models.BooleanField('Черновик', default=True)
    image = models.ImageField('Изображение', upload_to='images/services/', blank=True)
    slug = models.SlugField('url', db_index=True, unique=True)
    article = CKEditor5Field('Статья', config_name='extends', blank=True)
    time_update = models.DateTimeField('Дата изменения', auto_now=True)

    def __str__(self):
        return self.header

    def get_absolute_url(self):
        return reverse('home:service', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
