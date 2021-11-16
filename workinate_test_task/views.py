import os
from django.shortcuts import render
from .forms import SearchForm
from .settings import TEMPLATE_DIR


def index(request):
    return render(request,
                  os.path.join(TEMPLATE_DIR, 'index.html'),
                  {'title': 'Starting page', 'forms': [('Yandex', SearchForm()),
                                                       ('Google', SearchForm())]})