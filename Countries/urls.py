from django.urls import path
from MainApp import views

urlpatterns = [
    path('', views.home),
    path('countries-list/', views.countries_list),
    path('languages-list/', views.languages),
    path('languages-list/<str:language>', views.languages_countries),
    path('countries-list/<str:country_name>', views.country),
    path('countries-list/speaking-countries/<str:language>', views.language_in_countries)
]
