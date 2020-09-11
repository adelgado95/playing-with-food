from django.views.generic.base import TemplateView
from django.template import loader
from app.recipes.models import Receta
from django.shortcuts import render

class IndexView(TemplateView):
    template_name = 'index/index.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

def recipe_view(request, slug):
    print(slug)
    recipe = Receta.objects.get(slug=slug)
    context = {
        'recipe': recipe,
    }

    return render(request, 'index/recipe.html', context)