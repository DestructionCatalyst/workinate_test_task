from django.urls import path
from .views import search_yandex, search_google


urlpatterns = [
    path('yandex', search_yandex, name='Yandex search'),
    path('google', search_google, name='Google search')
]