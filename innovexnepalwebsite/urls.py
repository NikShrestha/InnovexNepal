from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Root URL for the index view
    path('about/', views.about, name='about'),
    path('about', views.about, name='about'),
    path('index/', views.index, name='index'),
    path('index', views.index, name='index'),
    path('services', views.services, name='services'),
    path('services/', views.services, name='services'),
    path('contact', views.contact, name='contact'),
    path('contact/', views.contact, name='contact'),
]
