from django.conf.urls import include
from django.urls import path,re_path
from app.index import views

urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
	path('services/', views.ServicesView.as_view(), name='index'),
	re_path('recipe/(?P<slug>\D+)/', views.recipe_view, name='recipes-recipe'),
]