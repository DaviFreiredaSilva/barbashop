from django.shortcuts import render, redirect
from .forms import CadastroForm, LoginForm
from .models import User
from django import forms
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

def cadastro(request):
    if request.method == 'POST':
        form=CadastroForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            email = cd['email']
            if cd['nome']:
                nome = cd['nome']
            else:
                nome=''
            cep = cd['cep']
            endereco = cd['endereco']
            if cd['telefone']:
                telefone = cd['telefone']
            else:
                telefone = ''
            senha = cd['senha']
            confirme = cd['confirme']
            if senha != confirme:
                raise forms.ValidationError('A senha de confirmação está diferente da senha digitada.')
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError('O email digitado já está cadastrado.')
            else:
                user = User(
                email=email, nome=nome, cep=cep, endereco=endereco, telefone=telefone, 
            )
                user.set_password(senha)
                user.save()
        
    form = CadastroForm()
    context = {
        'form':form
    }
    return render(request, 'contas/cadastro.html', context)

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, email=cd['email'], password = cd['password'],)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('loja:index')
                else:
                    return HttpResponse('Conta dessativada')
            else:
                return HttpResponse('Login inválido')
    else:
        form=LoginForm()
    context={
        'form':form
    }
    return render(request, 'registration/login.html', context)

def logout(request):
    return render(request, 'contas/logout.html')

def dashboard(request):
    if request.user.is_authenticated:
        nome_usuario = request.user.email.split('@')[0]
        context = {
            'nome_usuario': nome_usuario
        }
    else:
        context= {}
    
    return render(request, 'registration/dashboard.html', context)