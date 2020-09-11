from django.conf.urls import include
from django.urls import path
from app.recipes import views

urlpatterns = [
    path('<slug:slug>/', views.RecipeView.as_view(), name='recipes-recipe'),
]
	
