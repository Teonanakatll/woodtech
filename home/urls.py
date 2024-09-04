from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('all_projects/<str:slug>/', views.projects, name='projects'),
    path('all_projects/project/<str:slug>/', views.project_article, name='project'),
    path('services/<str:slug>/', views.services, name='services'),
    path('services/service/<str:slug>/', views.service_article, name='service'),
    path('our_blogs/<str:slug>/', views.blog, name='blog'),
    path('our_blogs/blog/<str:slug>/', views.blog_article, name='article'),
    path('our_company/<str:slug>/', views.company, name='company'),

    # боковое меню
    path('benefits/benefit/<str:slug>/', views.benefit_article, name='benefit'),
    path('benefits/<str:slug>/', views.benefits, name='benefits'),
    path('partners/<str:slug>/', views.partners, name='partners'),
    path('feedback/<str:slug>/', views.feedback, name='feedback'),
]
