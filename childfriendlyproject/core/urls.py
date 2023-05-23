from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.homepage, name='home'), 
    path('contact/', views.contactpage, name='contact'),
    path('place/', views.placepage, name='place'),
]
