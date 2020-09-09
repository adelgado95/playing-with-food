from django.db import models
from app.res.models import ActiveInactive
import logging

logger = logging.getLogger(__name__)


class Categoria(ActiveInactive):
    nombre = models.SlugField(max_length=50)
    orden = models.IntegerField(default=100)
    descripcion = models.CharField(null=True, blank=True, max_length=300)
    visitas = models.IntegerField(default=1, editable=False)


#     def save(self, update_cache=True, *args, **kwargs):
#         super(CategoriaTag, self).save(*args, **kwargs)
#         if update_cache:
#             get_home_data_cache(force_update=True)

#     def image_tag(self):
#         from django.utils.html import mark_safe
#         return mark_safe('<img src="/media/%s" width="50" height="50" />' % (self.imagen.name))

#     image_tag.short_description = 'Imagen Preview'

#     @property
#     def tiene_tags_con_negocios(self):
#         for tag in self.tag_set.all():
#             if tag.tiene_negocios_activos:
#                 return True
#         return False

#     @property
#     def get_tags_string(self):
#         return ','.join([t.nombre for t in self.tag_set.all()])

#     @property
#     def get_tags_dict(self):
#         return [ t.as_dict for t in self.tag_set.all().order_by('nombre') if t.tiene_negocios_activos ]

#     @property
#     def get_all_tags_dict(self):
#         return [ t.as_dict for t in self.tag_set.all().order_by('nombre') ]

#     @property
#     def get_negocios_count(self):
#         return sum([n.get_negocios_count for n in self.tag_set.all()])

#     def increment_visitas_counter(self):
#         self.visitas += 1
#         self.save(update_cache=False)


#     @property
#     def as_dict(self):
#         return {
#             'id': self.pk,
#             'nombre': self.nombre,
#             'descripcion': self.descripcion,
#             'orden': self.orden,
#             'navegable': self.navegable,
#             'imagen': ( settings.MEDIA_SERVER + self.imagen.url ) if self.imagen else '',
#         }

    
#     class Meta:
#         verbose_name = u'Categoría de Tags'
#         verbose_name_plural = u'Categorías de Tags'

#     def __str__(self):
#         return self.nombre

# class Tag(models.Model):
#     nombre = models.CharField(max_length=50)
#     orden = models.IntegerField(null=True, blank=True)
#     categoria = models.ForeignKey(CategoriaTag, on_delete=models.PROTECT, verbose_name=u'Clasificación')
#     imagen = models.ImageField(max_length=200, help_text=u"Resolución optima 50x50 px", blank=True, null=True)
#     visitas = models.IntegerField(default=1, editable=False)

#     class Meta:
#         verbose_name = u'Tag Negocio'
#         verbose_name_plural = u'Tags Negocio'

#     def __str__(self):
#         return self.nombre

#     def save(self, update_cache=True, *args, **kwargs):
#         super(Tag, self).save(*args, **kwargs)
#         if update_cache:
#             get_home_data_cache(force_update=True)


#     def increment_visitas(self):
#         self.visitas += 1
#         self.save(update_cache=False)

#     @property
#     def tiene_negocios_activos(self):
#         for n in self.negocio_set.filter(estado=True):
#             if n.estado:
#                 return True
#         return False

#     def image_tag(self):
#         from django.utils.html import mark_safe
#         return mark_safe('<img src="/media/%s" width="50" height="50" />' % (self.imagen.name))

#     image_tag.short_description = 'Imagen Preview'


#     @property
#     def get_negocios_dict(self):
#         return [ n.as_dict for n in self.negocio_set.filter(estado=True) ]

#     @property
#     def get_negocios_count(self):
#         return len([n.pk for n in self.negocio_set.filter(estado=True)])

#     @property
#     def as_dict(self):
#         imagen = ''
#         if not self.imagen:
#             imagen = settings.MEDIA_SERVER + self.categoria.imagen.url if self.categoria.imagen else ''
#         else:
#             imagen = settings.MEDIA_SERVER + self.imagen.url if self.imagen else ''

#         return {
#             'id': self.pk,
#             'nombre': self.nombre,
#             'imagen': imagen
#             }
    
# # @receiver(post_save, sender=Tag, dispatch_uid="update_from_tag")
# # @receiver(post_save, sender=CategoriaTag, dispatch_uid="update_from categoria")
# # def update_main_cache(sender, instance, created, **kwargs):
# #     logger.warning('Updating cache')
    
