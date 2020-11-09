from django.conf.urls import include, url
from django.urls import path,re_path
from app.reports import views	

urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
]