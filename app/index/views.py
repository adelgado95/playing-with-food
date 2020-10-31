from django.views.generic.base import TemplateView
from django.template import loader
from django.http import JsonResponse
from app.recipes.models import Receta
from app.blog.models import Entrada, MensajeContacto
from app.categories.models import Categoria
from django.shortcuts import render, redirect

from django.contrib.gis.geoip2 import GeoIP2
from django.views.decorators.csrf import csrf_exempt
import requests


class IndexView(TemplateView):
    template_name = 'index/index.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['categories'] = [ c for c in Categoria.objects.all() ]
        context['latest_blog'] = Entrada.objects.all().order_by('-fecha')[0]
        context['title'] = 'Home'
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
        'categories': [ c for c in Categoria.objects.all() ],
        'title': recipe.nombre
    }

    return render(request, 'index/recipe.html', context)

def recipe_view_by_id(request, id):
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
    recipe = Receta.objects.get(pk=id)
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


def blog_view(request):
    entries = Entrada.objects.all()
    context = {
        'entries': entries,
        'categories': [ c for c in Categoria.objects.all() ]
    }
    return render(request, 'index/blog.html', context)


class OGTags(TemplateView):
    """
    Get OG tags
    """
    template_name = 'og/og_tags_receta.html'

    @csrf_exempt
    def get(self, request, *args, **kwargs):
        from app.recipes.models import Receta

        try:
            # get params
            _entity = kwargs.get('slug')
            _pk = kwargs.get('pk')

            switch_set = self.switch_class
            cls = switch_set[_entity]['model']

            qs = {switch_set[_entity]['field']: _pk}

            data = cls.objects.get(**qs)

            self.template_name = 'og/og_tags_%s.html' % _entity

            # Packages lists
            return self.render_to_response({
                'data': data
            })
        except (Receta.DoesNotExist) as e:
            return JsonResponse({
                'status': False
            })

    @property
    def switch_class(self):
        """
        Return switch report types for agency
        :return:
        """
        from app.recipes.models import Receta

        # Type of report
        # beneficio = 0
        # establecimiento = 1
        # noticia = 2

        # Switch report type
        return {
            'receta': {
                'model': Receta,
                'field': 'pk'
            },
        }

@csrf_exempt
def contact_message(request):
    from mailjet_rest import Client
    name = request.POST.get('name','')
    lastname = request.POST.get('lastname','')
    topic = request.POST.get('topic','')
    message = request.POST.get('message','')
    api_key = 'ac187360edebf5560d72336576902b91'
    api_secret = '9293f3d69091470bf0792f6c74541910'
    mailjet = Client(auth=(api_key, api_secret), version='v3.1')
    created = MensajeContacto.objects.create(name=name,lastname=lastname, topic=topic, message=message)
    text = "Nombre: {0} \n Apellidos: {1} \n Asunto: {2} \n Mensaje: {3}".format(name, lastname, topic, message)

    data = {
    'Messages': [
        {
        "From": {
            "Email": "playingwithfoodni@gmail.com",
            "Name": "Automail"
        },
        "To": [
            {
            "Email": "playingwithfoodni@gmail.com",
            "Name": "Jessica"
            }
        ],
        "Subject": "Mensaje de Contacto Recibido",
        "TextPart": text,
        }
    ]
    }
    result = mailjet.send.create(data=data)
    print(result.status_code)
    print(result.json())
    return redirect('/')

