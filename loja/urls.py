from django.urls import path
from . import views

app_name='loja'

urlpatterns = [
    path('', views.index, name='index'),
    path('sobre/', views.sobre, name='sobre'),
    path('detalhes/<slug:slug>/', views.detalhe_produto, name='detalhe_produto'),
    path('produto/<slug:slug>/', views.produto_por_categoria, name='produto_por_categoria'),
    path('admin-produto/', views.admin_produto, name='admin_produto'),
    path('cadastro-produto/', views.cadastro_produto, name='cadastro_produto'),
]