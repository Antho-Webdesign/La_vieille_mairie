from django.urls import path
from restaurant.views import index, plat, carte

urlpatterns = [
    path('', index, name='index'),
    path('plat/', plat, name='plat'),
    path('carte/', carte, name='carte'),
    # path('categorie/', Header.as_view(), name='header'),
]
