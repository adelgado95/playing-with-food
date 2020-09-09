from django.db import models
from django.dispatch import receiver
import logging
from app.res.models import ActiveInactive

logger = logging.getLogger(__name__)


class Receta(ActiveInactive):
    nombre = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100)
    orden = models.IntegerField(default=100)
    imagen = models.ImageField(max_length=200, help_text=u"Resolución optima 50x50 px")
    visitas = models.IntegerField(default=1, editable=False)
    estado = models.BooleanField(default=True)
    proceso = models.TextField()


class Ingrediente(ActiveInactive):
    nombre = models.CharField(max_length=100)
    cantidad = models.CharField(max_length=50)
    receta = models.ForeignKey(Receta, on_delete=models.PROTECT)

