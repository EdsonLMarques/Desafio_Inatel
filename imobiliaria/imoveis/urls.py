from django.urls import path
from . import views
from .models import *

urlpatterns = [
    path('', views.home, name='home'),
    path('imovel/', views.cadastrar, name='cadastrar')
]