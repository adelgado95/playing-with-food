from django.db import models
from app.res.models import ActiveInactive
import logging

logger = logging.getLogger(__name__)


class Entrada(ActiveInactive):
    banner = models.ImageField()
    titulo = models.CharField(max_length=50)
    contenido = models.TextField()
    fecha = models.DateField()
    autor = models.CharField(max_length=100)
    visitas = models.IntegerField(default=1, editable=False)

    def get_absolute_url(self):
        return '/blog/entrada/{0}/'.format(self.pk)

    @property
    def get_paragraphs(self):
        return self.contenido.split('\n')

    @property
    def index_summarize(self):
        return self.contenido[:190] if len(self.contenido) > 190 else self.contenido
