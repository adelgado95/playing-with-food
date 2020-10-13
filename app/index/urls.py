from django.conf.urls import include, url
from django.urls import path,re_path
from app.index import views	

urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
	path('services/', views.ServicesView.as_view(), name='index'),
	#re_path('recipe/(?P<slug>\D+)/', views.recipe_view, name='recipes-recipe'),
	path('blog/entrada/<int:entrada_id>/', views.entrada_view, name='blog-entrada'),
	re_path('category/(?P<category>\D+)/', views.category_view, name='blog-entrada'),
	url(r'^recipe/(?P<slug>[\w-]+)/$', views.recipe_view, name='recipes-recipe'),
	url(r'^recipe/(?P<id>[\w-]+)/$', views.recipe_view_by_id, name='recipes-recipe'),
	path('category/', views.category_all_view, name='blog-entrada'),
	url(r'^og/(?P<slug>[\w-]+)/(?P<pk>\d+)/$', views.OGTags.as_view(), name='get_og_tags'),
]