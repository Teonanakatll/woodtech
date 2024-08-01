from django.shortcuts import render

def home(request):
    link_slug = 'index'
    return render(request, 'index.html', locals())
