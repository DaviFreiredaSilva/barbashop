from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from loja.models import Produto
from .cart import Cart
from .forms import CartAddProductForm
from django.contrib import messages

@require_POST
def cart_add(request, id_produto):
    cart = Cart(request)
    produto = get_object_or_404(Produto, id=id_produto)
    cart.adicionar(
            produto=produto,
            quantidade=1,
            override_quantity=None
        )
    messages.success(request, 'Produto adicionado ao carrinho.')    
    return redirect('loja:index')

@require_POST
def cart_remove(request, id_produto):
    cart = Cart(request)
    produto = get_object_or_404(Produto, id=id_produto)
    cart.remover(produto)
    return redirect('cart_detail')

def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={
            'quantidade':item['quantidade'],
            'override':True,
        })
    context = {
        'cart':cart
    }
    return render(request, 'cart/detail.html', context)

def cart_clear(request):
    cart = Cart(request)
    cart.limpar()
    
    return redirect('cart_detail')
