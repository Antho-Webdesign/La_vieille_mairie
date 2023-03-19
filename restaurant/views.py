from django.shortcuts import render
from django.views.generic import ListView

from restaurant.models import CategorieMenu


class Header(ListView):
    model = CategorieMenu
    template_engine = 'header'


def base(request):
    categorie = CategorieMenu.objects.all()
    context = {
        'categories': categorie,
    }
    return render(request, 'includes/header.html', context)


# Create your views here.
def index(request):
    return render(request, 'restaurant/index.html')
