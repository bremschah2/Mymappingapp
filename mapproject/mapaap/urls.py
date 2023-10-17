from django.urls import path
from . import views

urlpatterns = [
    path('map/', views.map_view, name='map'), 
    path('search/', views.search_view, name='search'),
    path('real-estate/', views.real_estate_view, name='real-estate'),
    path('', views.home_view, name='home'),
    path('contact/', views.contact_us, name='contact_us'),
    path('thank_you/', views.thank_you, name='thank_you'),
    path('currency/', views.currency_exchange_view, name='currency'),  # Add this line
    path('weather/<str:city>/', views.get_weather, name='get_weather'),

]
