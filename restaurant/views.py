from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView

from restaurant.models import CategorieMenu


class Header(generic.ListView):
    model = CategorieMenu
    template_name = 'includes/header.html'

    def get_queryset(self):
        return CategorieMenu.objects.all()


def base(request):
    categorie = CategorieMenu.objects.all()
    context = {
        'categories': categorie,
    }
    return render(request, 'includes/header.html', context)


# Create your views here.
def index(request):
    categorie = CategorieMenu.objects.all()
    context = {
        'categories': categorie,
    }
    return render(request, 'restaurant/index.html', context)
