from django.contrib import admin
from .models import VisitaCategoria, VisitaHome, VisitaReceta, VisitaHomeBlog, VisitaBlog, VisitaServicios, VisitaHomeCategorias

class VisitaHomeAdmin(admin.ModelAdmin):
	pass

class VisitaHome2Admin(admin.ModelAdmin):
	pass

admin.site.register(VisitaHome, VisitaHome2Admin)
admin.site.register(VisitaCategoria, VisitaHomeAdmin)
admin.site.register(VisitaReceta, VisitaHomeAdmin)
admin.site.register(VisitaHomeBlog, VisitaHomeAdmin)
admin.site.register(VisitaBlog, VisitaHomeAdmin)
admin.site.register(VisitaServicios, VisitaHomeAdmin)
admin.site.register(VisitaHomeCategorias, VisitaHomeAdmin)

