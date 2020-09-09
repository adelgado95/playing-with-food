from django.db import models
from app.res.models import ActiveInactive
import logging

logger = logging.getLogger(__name__)


class Entrada(ActiveInactive):
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=50)
    contenido = models.TextField()
    visitas = models.IntegerField(default=1, editable=False)