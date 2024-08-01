from django.db import models

class MainInfo(models.Model):
    """ Основная информация о сайте, название, телефон и адресс"""
    big_word = models.CharField('Первое слово названия', max_length=30)
    thin_word = models.CharField('Второе слово', max_length=30)
    phone = models.CharField('Телефон', max_length=25)
    address = models.CharField('Адрес', max_length=150)
    is_published = models.BooleanField('Опубликовать', default=False)

    def __str__(self):
        return f'{self.big_word} {self.thin_word}'

    class Meta:
        verbose_name = 'Название сайта и контакты'


class MainMenu(models.Model):
    """Основное меню"""
    name = models.CharField('Название', max_length=25)
    header = models.CharField('Заголовок страницы', max_length=60, blank=True)
    description = models.TextField('Описание', blank=True)
    slug = models.SlugField('url', max_length=50, unique=True, db_index=True, default='')
    published = models.BooleanField('Опубликовано', default=False)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'