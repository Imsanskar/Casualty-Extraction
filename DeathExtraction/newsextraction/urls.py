from django.urls import path
from . import views


app_name = 'newsextraction'

#url paths for different pages
urlpatterns = [
	path('', views.index, name='home'),
    path('extraction/', views.extraction, name='extraction'),
    path('about_us/', views.about_us, name='about_us'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('search/', views.searchquery, name='searchquery'),
]