from django.urls import path
from restaurant.views import index, plat

urlpatterns = [
    path('', index, name='index'),
    path('plat/', plat, name='plat'),
    # path('categorie/', Header.as_view(), name='header'),
]
