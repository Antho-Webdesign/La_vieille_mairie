from django.shortcuts import render

from restaurant.models import CategorieMenu


def index(request):
    categorie = CategorieMenu.objects.all()
    context = {
        'categories': categorie,
    }
    return render(request, 'restaurant/index.html', context)


def plat(request):
    return render(request, 'restaurant/plats.html')


'''

class CategorieMenuListView(generic.ListView):
    model = CategorieMenu

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(CategorieMenuListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['categories'] = categories
        return context

'''
