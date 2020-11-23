import requests

from django.http import JsonResponse

from app.recipes.models import Receta
from app.blog.models import Entrada, MensajeContacto
from app.categories.models import Categoria
from app.visits.models import VisitaCategoria, VisitaHome, VisitaReceta, VisitaHomeBlog, VisitaBlog, VisitaServicios, VisitaHomeCategorias
from django.db.models.functions import TruncDay
from django.db.models import Count
from app.config.models import IndexConfig, ServiciosConfig
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Sum
from pwfbackend import settings
import logging

logger = logging.getLogger(__name__)

#City.objects.values('country__name') \
#  .annotate(country_population=Sum('population')) \
#  .order_by('-country_population')

@csrf_exempt
def reports_views(request):
    import pandas as pd
    #logger.warning("Hello")
    #logger.warning(request.POST)
    page = request.POST['selectPaginas']
    month = request.POST['selectMonth']
    year = request.POST['selectYear']
    ttype = request.POST['selectTipo']
    parameter = request.POST['selectParameter']

    class_dict = {
        'VisitaCategoria':VisitaCategoria,
        'VisitaHome':VisitaHome,
        'VisitaReceta':VisitaReceta,
        'VisitaHomeBlog':VisitaHomeBlog,
        'VisitaBlog':VisitaBlog,
        'VisitaServicios':VisitaServicios,
        'VisitaHomeCategorias':VisitaHomeCategorias
    }
    result = {}
    logger.warning(page)
    cls = class_dict[page]
    data = cls.objects.filter(date_time__year=int(year),date_time__month=int(month))
    dict_data = [
        d.to_dict
        for d in data
    ]

    if len(dict_data) > 0:
        logger.warning(dict_data)
        df = pd.DataFrame.from_dict(dict_data)
        if parameter == 'total':
            result['result'] = df.groupby('date').size().to_dict()
        if parameter == 'country':
            result['result'] = df.groupby('country').size().to_dict()
        if parameter == 'os':
            result['result'] = df.groupby('os_family').size().to_dict()
        if parameter == 'device':
            bot= 0
            mobile = 0
            pc = 0
            tablet = 0
            for d in data:
                if d.is_bot:
                    bot = bot +1 
                if d.is_mobile:
                    mobile = mobile +1 
                if d.is_pc:
                    pc = pc +1 
                if d.is_tablet:
                    tablet = tablet +1
            result['result'] = {'bot':bot,'tablet':tablet,'pc':pc,'mobile':mobile} 
        labels = [ k for k,v in result['result'].items() ]
        values =  [ v for k,v in result['result'].items() ]
        result['labels'] = labels
        result['data'] = values
        logger.warning(data)

    return JsonResponse({'status': 'ok', 'data': result }, safe=False)
