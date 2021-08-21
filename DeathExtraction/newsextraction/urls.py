from django.urls import path
from . import views


app_name = 'newsextraction'

#url paths for different pages
urlpatterns = [
	path('', views.index, name='home'),
    path('extraction/', views.extraction, name='extraction'),
    path('graph/', views.graph, name='graph'),
    path('search/', views.searchView, name='searchview'),
]