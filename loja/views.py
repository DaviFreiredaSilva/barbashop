from django.shortcuts import render
from .models import Produto

def index(request):
    nome_usuario = ''
    produtos = Produto.objects.all()
    if request.user.is_authenticated:
        nome_usuario = request.user.email.split('@')[0]

    context = {
        'produtos':produtos,
        'nome_usuario':nome_usuario,
    }
    return render(request, 'loja/index.html', context)

def sobre(request):
    return render(request, 'loja/sobre.html')

def detalhe_produto(request, id):
    return render(request, 'loja/detalhe_produto.html')

def produto_por_categoria(request, slug):
    return render(request, 'loja/produto_por_categoria.html')