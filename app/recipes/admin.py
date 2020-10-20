from django.contrib import admin
from .models import Receta, SubReceta

class RecetaAdmin(admin.ModelAdmin):
	list_display = ('id', 'nombre', 'slug', 'categoria')

class SubRecetaAdmin(admin.ModelAdmin):
	pass



admin.site.register(Receta, RecetaAdmin)
admin.site.register(SubReceta, SubRecetaAdmin)