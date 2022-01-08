from django.urls import path
from . import views
from .models import *

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastrar_imovel', views.cadastrar, name='cadastrar'),
    path('<int:imovel_id>', views.imovel, name='imovel')
]