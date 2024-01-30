from django.urls import path
from . import views

app_name='loja'

urlpatterns = [
    path('', views.index, name='index'),
    path('sobre/', views.sobre, name='sobre'),
    path('detalhes/<int:id>/', views.detalhe_produto, name='detalhe_produto'),
    path('produto/<int:id>/', views.produto_por_categoria, name='produto_por_categoria'),
    path('admin-produto/', views.admin_produto, name='admin_produto'),
    path('cadastro-produto/', views.cadastro_produto, name='cadastro_produto'),
    path('editar-produto/<int:id>', views.editar_produto, name='editar_produto'),
    path('cadastro-categoria', views.cadastro_categoria, name='cadastro_categoria'),
]