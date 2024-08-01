from django.contrib import admin

from home.models import MainInfo, MainMenu


@admin.register(MainInfo)
class MainInfoAdmin(admin.ModelAdmin):
    list_display = ('big_word', 'thin_word', 'phone', 'address', 'is_published')

@admin.register(MainMenu)
class MainMenuAdmin(admin.ModelAdmin):
    list_display = ('name','slug', 'header', 'published')
    list_editable = ('published',)
    prepopulated_fields = {'slug': ('name',)}