from django.contrib import admin
from .models import Receta, SubReceta

class RecetaAdmin(admin.ModelAdmin):
	pass

class SubRecetaAdmin(admin.ModelAdmin):
	pass



admin.site.register(Receta, RecetaAdmin)
admin.site.register(SubReceta, SubRecetaAdmin)