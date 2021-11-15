from django.urls import path
from .views import search_yandex, search_google, search_serpapi_yandex


urlpatterns = [
    path('yandex', search_serpapi_yandex, name='Yandex search'),
    path('yandex_xml', search_yandex, name='Yandex XML search'),
    path('google', search_google, name='Google search')
]