from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastrar/', views.criar_prato, name='criar_prato'),
    path('pedir/', views.criar_pedido, name='criar_pedido'),
]