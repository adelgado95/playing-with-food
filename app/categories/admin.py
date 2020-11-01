from django.contrib import admin
from .models import Categoria, UserAgent


class CategoriaAdmin(admin.ModelAdmin):
	pass

class UserAgentAdmin(admin.ModelAdmin):
	pass


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(UserAgent, UserAgentAdmin)
