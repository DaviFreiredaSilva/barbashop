from django.shortcuts import render, redirect
from .models import Produto, Categoria
from decimal import Decimal
from cart.cart import Cart

def index(request):
    nome_usuario = ''
    produtos = Produto.objects.all()
    categorias = Categoria.objects.all()
    if request.user.is_authenticated:
        nome_usuario = request.user.email.split('@')[0]

    #Filtros de produtos
    if request.method == 'POST':
        #Filtro por ordem
        if request.POST.get('filtro-ordem'):
            filtro_ordem = request.POST.get('filtro-ordem')
            if filtro_ordem == 'recente':
                produtos = Produto.objects.all().order_by('created')
            if filtro_ordem == 'menor':
                produtos = Produto.objects.all().order_by('preco')
            if filtro_ordem == 'maior':
                produtos = Produto.objects.all().order_by('-preco')
                
         #Filtro por categoria   
        if request.POST.get('filtro-categoria'):
            print(request.POST.get('filtro-categoria'))
            filtro_categoria = request.POST.get('filtro-categoria')
            if filtro_categoria == 'todas':
                pass
            else:
                categoria = Categoria.objects.get(nome = filtro_categoria)
                produtos = Produto.objects.filter(categoria=categoria)
        
        context = {
            'produtos':produtos,
            'categorias':categorias,
            'nome_usuario':nome_usuario,
        }
        return render(request, 'loja/index.html', context)
    else:  
        context = {
            'produtos':produtos,
            'categorias':categorias,
            'nome_usuario':nome_usuario,
        }
    return render(request, 'loja/index.html', context)

def sobre(request):
    return render(request, 'loja/sobre.html')

def detalhe_produto(request, slug):
    produto = Produto.objects.get(slug=slug)
    context = {
        'produto':produto
    }
    return render(request, 'loja/detalhe_produto.html', context)

def produto_por_categoria(request, slug):
    return render(request, 'loja/produto_por_categoria.html')

def admin_produto(request):
    produtos = Produto.objects.all()
    context = {
        'produtos':produtos
    }
    return render(request, 'loja/admin-produto.html', context)

def cadastro_produto(request):
    categorias = Categoria.objects.all()
    if request.method == 'POST':
        nome = request.POST['nome']
        slug = nome.replace(" ", '-')
        if request.POST['categoria']:
            categoria = Categoria.objects.get(nome=request.POST['categoria'])
        else:
            categoria=None
        if request.POST['descricao']:
            descricao = request.POST['descricao']
        else:
            descricao=None
        #strpreco = str(request.POST['preco']).replace(",",".")
        #preco = Decimal(strpreco)
        preco = request.POST['preco']
        if request.FILES:
            imagem = request.FILES['imagem']
        else:
            imagem=None     
               
        produto = Produto(
            nome = nome,
            slug = slug,
            categoria = categoria,
            descricao = descricao,
            preco = preco,
            imagem = imagem
        )
        produto.save()
        
    context={
        'categorias':categorias
    }
    return render(request, 'loja/cadastro-produto.html', context)
