from django.db import models
from django.dispatch import receiver
import logging
from app.res.models import ActiveInactive
import datetime

logger = logging.getLogger(__name__)


class Receta(ActiveInactive):
    nombre = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100)
    categoria = models.ForeignKey('categories.Categoria', on_delete=models.PROTECT)
    orden = models.IntegerField(default=100)
    imagen = models.ImageField()
    preview = models.ImageField()
    visitas = models.IntegerField(default=1, editable=False)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateField(default=datetime.date.today)
    ingredientes = models.TextField()
    preparacion = models.TextField()

    def get_absolute_url(self):
        return 'recipe/{0}/'.format(self.slug)

    def __str__(self):
        return self.nombre

    @property
    def get_absolute_url(self):
        return '/recipe/{0}'.format(self.slug)
    
    @property
    def get_sub_recipes(self):
        return [
            subReceta
            for subReceta in self.subreceta_set.all()
        ]

    @property
    def get_ingredients(self):
        return [
            ingrediente
            for ingrediente in self.ingredientes.splitlines()
        ]
    
    @property
    def get_pasos_preparacion(self):
        return [
            paso
            for paso in self.preparacion.splitlines()
        ]

    @property
    def get_last_recipes(self):
        erased = False
        recipes = [ 
            { 
                'id': r.pk,
                'title': r.nombre, 
                'imagen': r.imagen.url ,
                'preview': r.preview.url,
                'url': r.get_absolute_url
            } 
            for r in Receta.objects.all().order_by('-fecha_creacion')[:4] 
        ]
        for r in recipes:
            if r['id'] == self.pk:
                recipes.remove(r)
                erased = True
        if not erased:
            recipes.pop()
        return recipes            


class SubReceta(ActiveInactive):
    nombre = models.CharField(max_length=50)
    receta = models.ForeignKey(Receta, on_delete=models.PROTECT)
    ingredientes = models.TextField()


    def __str__(self):
        return self.nombre

    @property
    def get_ingredients(self):
        return [
            ingrediente
            for ingrediente in self.ingredientes.splitlines()
        ]
