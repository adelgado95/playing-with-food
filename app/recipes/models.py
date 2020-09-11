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
    imagen = models.ImageField(max_length=200, help_text=u"Resolución optima 50x50 px")
    visitas = models.IntegerField(default=1, editable=False)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateField(default=datetime.date.today)


    def __str__(self):
        return self.nombre
    
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
            for ingrediente in self.ingrediente_set.all()
        ]
    
    @property
    def get_pasos_preparacion(self):
        return [
            paso
            for paso in self.paso_set.all().order_by('numero')
        ]

class Ingrediente(ActiveInactive):
    nombre = models.CharField(max_length=100)
    cantidad = models.CharField(max_length=50)
    receta = models.ForeignKey(Receta, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre


class SubReceta(ActiveInactive):
    nombre = models.CharField(max_length=50)
    receta = models.ForeignKey(Receta, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre

    @property
    def get_ingredients(self):
        return [
            ingrediente
            for ingrediente in self.subrecetaingrediente_set.all()
        ]


class SubRecetaIngrediente(ActiveInactive):
    nombre = models.CharField(max_length=100)
    cantidad = models.CharField(max_length=50)
    subreceta = models.ForeignKey(SubReceta, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre

class Paso(ActiveInactive):
    numero = models.IntegerField()
    descripcion = models.TextField()
    receta = models.ForeignKey(Receta, on_delete=models.PROTECT)

