from django.db import models
from app.res.models import ActiveInactive
import logging

logger = logging.getLogger(__name__)


class Categoria(ActiveInactive):
    nombre = models.SlugField(max_length=50)
    orden = models.IntegerField(default=100)
    descripcion = models.CharField(null=True, blank=True, max_length=300)
    visitas = models.IntegerField(default=1, editable=False)

    def __str__(self):
        return self.nombre



