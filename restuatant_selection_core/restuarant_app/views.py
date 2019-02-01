# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'restuarant_app/index.html', {'text': "hello world"})


def suggestions(request):
    return render(request, 'restuarant_app/suggestions.html', {})


def about_us(request):
    return render(request, 'restuarant_app/about.html', {})
