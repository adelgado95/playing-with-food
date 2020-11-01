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


class UserAgent(models.Model):
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

