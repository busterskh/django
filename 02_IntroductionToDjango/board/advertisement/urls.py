from django.urls import path
from .import views

urlpatterns = [
    path("", views.advertisement_list,  name='advertisement_list'),
    path("python_basic/", views.python_basic, name='python_basic'),
    path("python_advanced/", views.python_advanced, name='python_advanced'),
    path("django/", views.django, name='django'),
    path("mysql/", views.mysql, name='MySQL'),
    path("html/", views.html, name='HTML')

]
