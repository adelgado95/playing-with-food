import requests

from django.views.generic.base import TemplateView
from django.template import loader
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.gis.geoip2 import GeoIP2
from django.views.decorators.csrf import csrf_exempt

from app.recipes.models import Receta
from app.blog.models import Entrada, MensajeContacto
from app.categories.models import Categoria
from app.visits.models import VisitaCategoria, VisitaHome, VisitaReceta, VisitaHomeBlog, VisitaBlog, VisitaServicios, VisitaHomeCategorias

from pwfbackend import settings



class IndexView(TemplateView):
    template_name = 'index/index.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        self.registry_user_agent(request)
        context['categories'] = [ c for c in Categoria.objects.all() ]
        context['latest_blog'] = Entrada.objects.all().order_by('-fecha')[0]
        context['title'] = 'Home'

        return self.render_to_response(context)

    def registry_user_agent(self, request):
        from app.visits.models import VisitaHome
        print(request.user_agent.os.version_string)
        country = get_country_from_request(request)
        VisitaHome.objects.create(
            is_mobile = request.user_agent.is_mobile,
            is_tablet = request.user_agent.is_tablet,
            is_touch_capable = request.user_agent.is_touch_capable,
            is_pc = request.user_agent.is_pc,
            is_bot = request.user_agent.is_bot,
            browser_family = request.user_agent.browser.family,
            browser_version = request.user_agent.browser.version_string,
            os_family = request.user_agent.os.family,
            os_version = request.user_agent.os.version_string,
            device_family =  request.user_agent.device.family,
            country=country
        )


class ServicesView(TemplateView):
    template_name = 'index/services.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        self.registry_user_agent(request)
        context['categories'] = [ c for c in Categoria.objects.all() ]
        return self.render_to_response(context)

    def registry_user_agent(self, request):
        VisitaServicios.objects.create(
            is_mobile = request.user_agent.is_mobile,
            is_tablet = request.user_agent.is_tablet,
            is_touch_capable = request.user_agent.is_touch_capable,
            is_pc = request.user_agent.is_pc,
            is_bot = request.user_agent.is_bot,
            browser_family = request.user_agent.browser.family,
            browser_version = request.user_agent.browser.version_string,
            os_family = request.user_agent.os.family,
            os_version = request.user_agent.os.version_string,
            device_family =  request.user_agent.device.family
        )   

def recipe_view(request, slug):
    print(slug)
    g = GeoIP2()
    print(request.META)
    country = get_country_from_request(request)

    print("Printing country")
    print(country)
    recipe = Receta.objects.get(slug=slug)
    VisitaReceta.objects.create(
            is_mobile = request.user_agent.is_mobile,
            is_tablet = request.user_agent.is_tablet,
            is_touch_capable = request.user_agent.is_touch_capable,
            is_pc = request.user_agent.is_pc,
            is_bot = request.user_agent.is_bot,
            browser_family = request.user_agent.browser.family,
            browser_version = request.user_agent.browser.version_string,
            os_family = request.user_agent.os.family,
            os_version = request.user_agent.os.version_string,
            device_family =  request.user_agent.device.family,
            receta = recipe,
            country=country
        )  
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
    VisitaReceta.objects.create(
            is_mobile = request.user_agent.is_mobile,
            is_tablet = request.user_agent.is_tablet,
            is_touch_capable = request.user_agent.is_touch_capable,
            is_pc = request.user_agent.is_pc,
            is_bot = request.user_agent.is_bot,
            browser_family = request.user_agent.browser.family,
            browser_version = request.user_agent.browser.version_string,
            os_family = request.user_agent.os.family,
            os_version = request.user_agent.os.version_string,
            device_family =  request.user_agent.device.family,
            receta = recipe
        )  
    context = {
        'recipe': recipe,
        'categories': [ c for c in Categoria.objects.all() ]
    }

    return render(request, 'index/recipe.html', context)

def entrada_view(request, entrada_id):
    entrada = Entrada.objects.get(pk=entrada_id)
    VisitaBlog.objects.create(  
            is_mobile = request.user_agent.is_mobile,
            is_tablet = request.user_agent.is_tablet,
            is_touch_capable = request.user_agent.is_touch_capable,
            is_pc = request.user_agent.is_pc,
            is_bot = request.user_agent.is_bot,
            browser_family = request.user_agent.browser.family,
            browser_version = request.user_agent.browser.version_string,
            os_family = request.user_agent.os.family,
            os_version = request.user_agent.os.version_string,
            device_family =  request.user_agent.device.family,
            entrada = entrada
            )
    context = {
        'entrada': entrada,
        'categories': [ c for c in Categoria.objects.all() ]
    }

    return render(request, 'index/blog_entrada.html', context)


def category_view(request, category):
    category = Categoria.objects.get(nombre=category)
    recipes = Receta.objects.filter(categoria=category)
    VisitaCategoria.objects.create(  
            is_mobile = request.user_agent.is_mobile,
            is_tablet = request.user_agent.is_tablet,
            is_touch_capable = request.user_agent.is_touch_capable,
            is_pc = request.user_agent.is_pc,
            is_bot = request.user_agent.is_bot,
            browser_family = request.user_agent.browser.family,
            browser_version = request.user_agent.browser.version_string,
            os_family = request.user_agent.os.family,
            os_version = request.user_agent.os.version_string,
            device_family =  request.user_agent.device.family,
            categoria = category
            )
    context = {
        'recipes': recipes,
        'categories': [ c for c in Categoria.objects.all() ]
    }
    return render(request, 'index/category.html', context)

def category_all_view(request):
    recipes = Receta.objects.all()
    VisitaHomeCategorias.objects.create(  
            is_mobile = request.user_agent.is_mobile,
            is_tablet = request.user_agent.is_tablet,
            is_touch_capable = request.user_agent.is_touch_capable,
            is_pc = request.user_agent.is_pc,
            is_bot = request.user_agent.is_bot,
            browser_family = request.user_agent.browser.family,
            browser_version = request.user_agent.browser.version_string,
            os_family = request.user_agent.os.family,
            os_version = request.user_agent.os.version_string,
            device_family =  request.user_agent.device.family
            )
    context = {
        'recipes': recipes,
        'categories': [ c for c in Categoria.objects.all() ]
    }
    return render(request, 'index/category.html', context)


def blog_view(request):
    entries = Entrada.objects.all()
    VisitaHomeBlog.objects.create(  
            is_mobile = request.user_agent.is_mobile,
            is_tablet = request.user_agent.is_tablet,
            is_touch_capable = request.user_agent.is_touch_capable,
            is_pc = request.user_agent.is_pc,
            is_bot = request.user_agent.is_bot,
            browser_family = request.user_agent.browser.family,
            browser_version = request.user_agent.browser.version_string,
            os_family = request.user_agent.os.family,
            os_version = request.user_agent.os.version_string,
            device_family =  request.user_agent.device.family
            )
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
    email = request.POST.get('correo','')
    topic = request.POST.get('topic','')
    message = request.POST.get('message','')
    api_key = settings.MAILJET_APIKEY 
    api_secret = settings.MAILJET_APISECRET 
    mailjet = Client(auth=(api_key, api_secret), version='v3.1')
    created = MensajeContacto.objects.create(name=name,email=email, topic=topic, message=message)
    text = "Nombre: {0} \n Correo: {1} \n Asunto: {2} \n Mensaje: {3}".format(name, email, topic, message)

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

def get_country_from_request(request):
    country = None
    try:
        ip = get_client_ip(request)
        country = get_data_by_ip(ip)['country_name']
    except:
        country='Nicaragua'
    return country

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]        
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def get_data_by_ip(ip):
    api_key = settings.IP_DATA_APIKEY
    url = 'https://api.ipdata.co/{0}?api-key={1}'.format(ip, api_key)
    r = requests.get(url)
    return r.json()
