from django.contrib import admin
from .models import Receta, Ingrediente, SubRecetaIngrediente, SubReceta, Paso

class IngredienteInlineAdmin(admin.StackedInline):
	model = Ingrediente
	can_delete = True
	fk_name = 'receta'
	extra = 1

class PasoInlineAdmin(admin.StackedInline):
	model = Paso
	can_delete = True
	fk_name = 'receta'
	extra = 1

class IngredienteInlineAdmin(admin.StackedInline):
	model = Ingrediente
	can_delete = True
	fk_name = 'receta'
	extra = 1

class RecetaAdmin(admin.ModelAdmin):
	inlines = (IngredienteInlineAdmin, PasoInlineAdmin)

class IngredienteSubrecetaInlineAdmin(admin.StackedInline):
	model = SubRecetaIngrediente
	fk_name = 'subreceta'
	can_delete = True
	extra = 1

class SubRecetaAdmin(admin.ModelAdmin):
	inlines = (IngredienteSubrecetaInlineAdmin, )




admin.site.register(Receta, RecetaAdmin)
admin.site.register(SubReceta, SubRecetaAdmin)