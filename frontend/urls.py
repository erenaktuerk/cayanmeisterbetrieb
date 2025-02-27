from django.urls import path
from . import views

app_name='frontend'
urlpatterns = [
    path('leistung/', views.leistung, name='leistung'),
    path('kontakt/', views.kontakt, name='contact'),
    path('aboutus/', views.aboutus, name='aboutus'),

    #law stuff
    path('impressum/', views.impressum, name='impressum'),
    path('datenschutz/', views.datenschutz, name='datenschutz'),
    path('agb/', views.agb, name='agb'),



    path('', views.home, name='home')
]
