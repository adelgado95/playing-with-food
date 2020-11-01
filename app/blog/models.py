from django.db import models
from app.res.models import ActiveInactive
import logging
from ckeditor.fields import RichTextField



logger = logging.getLogger(__name__)


class Entrada(ActiveInactive):
    banner = models.ImageField()
    titulo = models.CharField(max_length=50)
    fecha = models.DateField()
    autor = models.CharField(max_length=100)
    visitas = models.IntegerField(default=1, editable=False)

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return '/blog/entrada/{0}/'.format(self.pk)

    @property
    def get_paragraphs(self):
        return self.contenido.split('\n')

    @property
    def index_summarize(self):
        from django.utils.html import mark_safe
        for content in self.get_contents:
            if content.tipo == 'texto':
                return content.contenido_texto[:190] if len(content.contenido_texto) > 190 else content.contenido_texto
                
        

    @property
    def get_contents(self):
        return  self.contenido_entrada.all().order_by('orden')


class Contenido(ActiveInactive):
    TIPO_CHOICES = (
        ('imagen','Imagen'),
        ('texto','Texto'),
    )
    orden = models.IntegerField(default=1)    
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    contenido_texto = RichTextField(blank=True,null=True)
    contenido_imagen = models.ImageField(null=True, blank=True)
    entrada = models.ForeignKey(Entrada, on_delete=models.CASCADE, related_name='contenido_entrada')

class MensajeContacto(ActiveInactive):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    topic = models.CharField(max_length=50)
    message = models.TextField()
    
