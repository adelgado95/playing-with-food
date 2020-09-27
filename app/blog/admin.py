from django.contrib import admin
from .models import Entrada


class EntradaAdmin(admin.ModelAdmin):
	pass


admin.site.register(Entrada, EntradaAdmin)
