from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('adicionar/<int:id_produto>/', views.cart_add, name='cart_add'),
    path('remover/<int:id_produto>/', views.cart_remove, name='cart_remove'),
    path('limpar', views.cart_clear, name='cart_clear'),
]