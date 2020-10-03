from django.views.generic.base import TemplateView
from django.template import loader
from app.recipes.models import Receta
from app.blog.models import Entrada
from app.categories.models import Categoria
from django.shortcuts import render
from django.contrib.gis.geoip2 import GeoIP2
import requests


class IndexView(TemplateView):
    template_name = 'index/index.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['categories'] = [ c for c in Categoria.objects.all() ]
        context['latest_blog'] = Entrada.objects.all().order_by('-fecha')[0]
        return self.render_to_response(context)

class ServicesView(TemplateView):
    template_name = 'index/services.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['categories'] = [ c for c in Categoria.objects.all() ]
        return self.render_to_response(context)


def recipe_view(request, slug):
    print(slug)
    g = GeoIP2()
    print(request.META)
    country = None
    try:
        ip = request.META.get('REMOTE_ADDR', None)
        if ip:
            country = g.country(ip)['country']
        else:
            country = 'Nicaragua'
    except:
        pass
    print("Printing country")
    print(country)
    recipe = Receta.objects.get(slug=slug)
    context = {
        'recipe': recipe,
        'categories': [ c for c in Categoria.objects.all() ]
    }

    return render(request, 'index/recipe.html', context)

def entrada_view(request, entrada_id):
    entrada = Entrada.objects.get(pk=entrada_id)
    context = {
        'entrada': entrada,
        'categories': [ c for c in Categoria.objects.all() ]
    }

    return render(request, 'index/blog_entrada.html', context)


def category_view(request, category):
    category = Categoria.objects.get(nombre=category)
    recipes = Receta.objects.filter(categoria=category)
    context = {
        'recipes': recipes,
        'categories': [ c for c in Categoria.objects.all() ]
    }
    return render(request, 'index/category.html', context)

def category_all_view(request):
    recipes = Receta.objects.all()
    context = {
        'recipes': recipes,
        'categories': [ c for c in Categoria.objects.all() ]
    }
    return render(request, 'index/category.html', context)