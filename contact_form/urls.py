from django.urls import path

from . import views

urlpatterns = [
    path('', views.contact, name='index'),
    path('thanks/', views.thanks, name='thanks'),
]
