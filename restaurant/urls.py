from django.urls import path

from restaurant.views import index, Header

urlpatterns = [
    path('', index, name='index'),
    path('categorie/', Header.as_view(), name='header'),
]
