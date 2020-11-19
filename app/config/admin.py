from django.contrib import admin
from .models import IndexConfig, ServiciosConfig

class IndexConfigAdmin(admin.ModelAdmin):
    pass

class ServiciosConfigAdmin(admin.ModelAdmin):
    pass

admin.site.register(IndexConfig, IndexConfigAdmin)
admin.site.register(ServiciosConfig, ServiciosConfigAdmin)