from django.contrib import admin
from .models import Receta, Ingrediente

class IngrdienteInlineAdmin(admin.StackedInline):
	model = Ingrediente
	can_delete = True
	fk_name = 'receta'
	extra = 1

class RecetaAdmin(admin.ModelAdmin):
	inlines = (IngrdienteInlineAdmin, )


admin.site.register(Receta, RecetaAdmin)