from django.shortcuts import render
from django.http import HttpResponse


def advertisement_list(request, *args, **kwargs):
    return render(request, 'advertisement/advertisement_list.html', {})


def python_basic(request, *args, **kwargs):
    return render(request, 'advertisement/python_basic.html', {})


def python_advanced(request, *args, **kwargs):
    return render(request, 'advertisement/python_advanced.html', {})


def django(request, *args, **kwargs):
    return render(request, 'advertisement/django.html', {})


def mysql(request, *args, **kwargs):
    return render(request, 'advertisement/MySQL.html', {})


def html(request, *args, **kwargs):
    return render(request, 'advertisement/Html.html', {})


