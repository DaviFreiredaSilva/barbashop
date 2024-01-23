from django.urls import path
from . import views

app_name='loja'

urlpatterns = [
    path('', views.index, name='index'),
    path('sobre/', views.sobre, name='sobre'),
    path('<int:id>/', views.detalhe_produto, name='detalhe_produto'),
    path('<slug:slug>/', views.produto_por_categoria, name='produto_por_categoria'),
]