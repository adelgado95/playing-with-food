from django.contrib import admin
from .models import Entrada, Contenido, MensajeContacto


class ContenidoInline(admin.StackedInline):
    model = Contenido
    can_delete = True
    verbose_name_plural = 'Contenidos'
    fk_name = 'entrada'
    extra = 1
class EntradaAdmin(admin.ModelAdmin):
	list_display = ('id', 'titulo', 'fecha','autor')
	inlines = (ContenidoInline,)
class MensajeContactoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'topic')

admin.site.register(Entrada, EntradaAdmin)
admin.site.register(MensajeContacto, MensajeContactoAdmin)
