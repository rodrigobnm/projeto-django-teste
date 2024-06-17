from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='app-home'),
    path('sobre/', views.sobre, name='app-sobre'),
    path('aba1/', views.aba1, name='app-aba1')
    ]
