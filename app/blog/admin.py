from django.contrib import admin
from .models import Entrada


class EntradaAdmin(admin.ModelAdmin):
	list_display = ('id', 'titulo', 'fecha','autor')


admin.site.register(Entrada, EntradaAdmin)
