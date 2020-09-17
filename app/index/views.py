from django.views.generic.base import TemplateView
from django.template import loader
from app.recipes.models import Receta
from django.shortcuts import render
from django.contrib.gis.geoip2 import GeoIP2


class IndexView(TemplateView):
    template_name = 'index/index.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

def recipe_view(request, slug):
    print(slug)
    g = GeoIP2()
    try:
        ip = request.META.get('REMOTE_ADDR', None)
        if ip:
            country = g.country(ip)['country']
        else:
            country = 'Italia'
    except:
        country = 'Italia'
    print("Printing country")
    print(country)
    recipe = Receta.objects.get(slug=slug)
    context = {
        'recipe': recipe,
    }

    return render(request, 'index/recipe.html', context)