from django.conf.urls import include
from django.urls import path
from app.index import views

urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
]
	
