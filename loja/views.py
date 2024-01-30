from django.shortcuts import render, redirect
from .models import Produto, Categoria
from decimal import Decimal
from cart.cart import Cart
from django.contrib import messages

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

def detalhe_produto(request, id):
    produto = Produto.objects.get(id=id)
    context = {
        'produto':produto
    }
    return render(request, 'loja/detalhe_produto.html', context)

def produto_por_categoria(request, id):
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
            categoria = categoria,
            descricao = descricao,
            preco = preco,
            imagem = imagem
        )
        produto.save()
        messages.success(request, 'Produto criado com sucesso.')
        return redirect('loja:index')
    context={
        'categorias':categorias
    }
    return render(request, 'loja/cadastro-produto.html', context)

def editar_produto(request, id):
    produto = Produto.objects.get(id=id)
    categorias = Categoria.objects.all()
    
    if request.method =='POST':
        nome = request.POST['nome']
        if request.POST['categoria']:
            categoria = Categoria.objects.get(nome=request.POST['categoria'])
        else:
            categoria=None
        if request.POST['descricao']:
            descricao = request.POST['descricao']
        else:
            descricao=None
        preco = request.POST['preco']    
        if request.FILES:
            imagem = request.FILES['imagem']
        else:
            imagem = produto.imagem
             
        produto.nome = nome
        produto.categoria = categoria
        produto.descricao = descricao
        produto.preco = preco
        produto.imagem = imagem
        
        produto.save()
        messages.success(request, 'Produto editado com sucesso.')
        return redirect('loja:detalhe_produto', id=produto.id)
        
    context = {
        'categorias':categorias,
        'produto':produto,
    }
    return render(request, 'loja/editar-produto.html', context)

def cadastro_categoria(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        categoria = Categoria(nome = nome)
        categoria.save()
        messages.success(request, 'Categoria criada com sucesso.')
        return redirect('loja:index')
    return render(request, 'loja/cadastro-categoria.html')
