from django.contrib import admin
from .models import Receta, SubReceta

class SubRecetaInline(admin.StackedInline):
    model = SubReceta
    can_delete = True
    verbose_name_plural = 'Sub Recetas'
    fk_name = 'receta'
    extra = 1

class RecetaAdmin(admin.ModelAdmin):
	list_display = ('id', 'nombre', 'slug', 'categoria')
	inlines = (SubRecetaInline,)


admin.site.register(Receta, RecetaAdmin)