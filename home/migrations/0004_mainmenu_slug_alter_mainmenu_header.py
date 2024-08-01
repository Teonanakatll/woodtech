# Generated by Django 5.0.7 on 2024-07-31 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_mainmenu'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainmenu',
            name='slug',
            field=models.SlugField(default='', unique=True, verbose_name='url'),
        ),
        migrations.AlterField(
            model_name='mainmenu',
            name='header',
            field=models.CharField(blank=True, max_length=60, verbose_name='Заголовок страницы'),
        ),
    ]
