from django.conf.urls import include, url
from django.urls import path,re_path
from app.api import views	

urlpatterns = [
	path('reports/', views.reports_views, name='reports-index'),
]