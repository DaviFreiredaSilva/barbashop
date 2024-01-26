from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('adicionar/<int:id_produto>/', views.cart_add, name='cart_add'),
    path('remover/<intid_produto>/', views.cart_remove, name='cart_remove'),
]