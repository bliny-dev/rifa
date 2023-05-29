from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib import auth

def cadastro(request):
    if request.method == "GET":
        # if request.user.is_authenticated:
        #     return redirect('/sorteio')
        
        if not request.user.is_superuser:
            return redirect('/auth/logar')

        return render(request, 'cadastro.html')
    elif request.method == "POST":
        email = request.POST.get('email')
        username = request.POST.get('username')
        senha = request.POST.get('password')
        confirmar_senha = request.POST.get('confirm-password')
        ativo = True

        if not senha == confirmar_senha:
            messages.add_message(request, constants.ERROR, 'As senhas não coincidem')
            return redirect('/auth/cadastro')

        if len(username.strip()) == 0 or len(senha.strip()) == 0:
            messages.add_message(request, constants.ERROR, 'Os campos não podem ser vazios')
            return redirect('/auth/cadastro')

        user = User.objects.filter(username=username)
        
        if user.exists():
            messages.add_message(request, constants.ERROR, 'Esse usuário já existe')
            return redirect('/auth/cadastro')

        try:
            user = User.objects.create_user(username=username,password=senha)
            user.save()
            return redirect('/auth/logar')
        except:
            messages.add_message(request, constants.ERROR, 'Error interno do servidor')
            return redirect('/auth/cadastro')

    
def logar(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/sorteio')

        return render(request, 'logar.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('password')

        usuario = auth.authenticate(username=username, password=senha)

        if not usuario:
            messages.add_message(request, constants.ERROR, 'Usuário ou senha invalidos, tente novamente')
            return redirect('/auth/logar')
        else:
            auth.login(request, usuario)
            return redirect('/sorteio')


def sair(request):
    auth.logout(request)
    return redirect('/auth/logar') 