from django.db import models
from app.res.models import ActiveInactive
import logging

logger = logging.getLogger(__name__)

class Visita(models.Model):
    is_mobile = models.BooleanField(default=False) 
    is_tablet = models.BooleanField(default=False) 
    is_touch_capable = models.BooleanField(default=False) 
    is_pc = models.BooleanField(default=False) 
    is_bot = models.BooleanField(default=False) 
    browser_family = models.CharField(max_length=50)
    browser_version = models.CharField(max_length=50)
    os_family = models.CharField(max_length=50)
    os_version = models.CharField(max_length=50)
    device_family = models.CharField(max_length=50)

class VisitaCategoria(Visita):
    categoria = models.ForeignKey(to='categories.Categoria', on_delete=models.PROTECT)

class VisitaHomeCategorias(Visita):
    pass
class VisitaHome(Visita):
    date_time = models.DateTimeField(auto_now_add=True, verbose_name='Fecha y Hora', null=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    
    @property
    def to_dict(self):
        return {
            'date': self.date_time.strftime("%d/%m/%Y"),
            'country': self.country,
            'is_mobile' : self.is_mobile, 
            'is_tablet' : self.is_tablet, 
            'is_pc' : self.is_pc,
            'is_bot' : self.is_bot, 
            'device_family' : self.device_family,
            'os_family': self.os_family
        }

class VisitaReceta(Visita):
    receta = models.ForeignKey(to='recipes.Receta', on_delete=models.PROTECT)
    date_time = models.DateTimeField(auto_now_add=True, verbose_name='Fecha y Hora', null=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    
    @property
    def to_dict(self):
        return {
            'date': self.date_time.strftime("%d/%m/%Y"),
            'country': self.country,
            'is_mobile' : self.is_mobile, 
            'is_tablet' : self.is_tablet, 
            'is_pc' : self.is_pc,
            'is_bot' : self.is_bot, 
            'device_family' : self.device_family,
            'os_family': self.os_family
        }

class VisitaHomeBlog(Visita):
    pass
class VisitaBlog(Visita):
    entrada = models.ForeignKey(to='blog.Entrada', on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True, verbose_name='Fecha y Hora', null=True)
    @property
    def to_dict(self):
        return {
            'date': self.date_time.strftime("%d/%m/%Y"),
            'country': 'Nicaragua',
            'is_mobile' : self.is_mobile,
            'is_tablet' : self.is_tablet,
            'is_pc' : self.is_pc,
            'is_bot' : self.is_bot,
            'device_family' : self.device_family,
            'os_family': self.os_family
        }


class VisitaServicios(Visita):
    pass
