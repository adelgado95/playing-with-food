from django.db import models
from django.dispatch import receiver
import logging
from app.res.models import ActiveInactive
import datetime
from pwfbackend import settings
import urllib.parse
from ckeditor.fields import RichTextField


logger = logging.getLogger(__name__)


class IndexConfig(models.Model):
    title = models.CharField(max_length=200)
    contenido_texto = RichTextField(blank=True,null=True)
    contenido_texto_movil = RichTextField(blank=True,null=True)

class ServiciosConfig(models.Model):
    imagen = models.ImageField(null=True, blank=True)
    subtitulo = RichTextField(max_length=200,blank=True,null=True)
    contenido_texto = RichTextField(blank=True,null=True)
    contenido_texto_movil = RichTextField(blank=True,null=True)