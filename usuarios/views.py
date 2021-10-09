from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import FormContato

def login(request):
    if request.method != 'POST':
        return render(request, 'usuarios/login.html')

    user_post = request.POST.get('user')
    senha = request.POST.get('senha')
    #lembrar_senha = request.POST.get('lembrar_senha')

    if not user_post or not senha:
        messages.error(request, 'Nenhum campo pode ficar vazio!')
        return render(request, 'usuarios/login.html')


    user = auth.authenticate(request,  username=user_post, password=senha)
    print(user)
    if not user:
        messages.error(request, 'E-mail ou senha estão incorretos!')
        return render(request, 'usuarios/login.html')
    else:
        auth.login(request, user)
        messages.success(request, 'Login realizado com sucesso!')
        return redirect('dashboard')


def logout(request):
    auth.logout(request)
    return redirect('login')


def register(request):
    if request.method != 'POST':
        return render(request, 'usuarios/register.html')

    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    user = request.POST.get('user')
    senha = request.POST.get('senha')
    repsenha = request.POST.get('repsenha')

    # print(request.POST)
    # print(nome)
    # print(sobrenome)
    # print(email)
    # print(user)
    # print(senha)
    # print(repsenha)

    if not nome or not sobrenome or not email or not user or not senha or not repsenha:
        messages.error(request, 'Nenhum campo pode ficar vazio!')
        return render(request, 'usuarios/register.html')

    if len(user) < 3:
        messages.error(request, 'Nome de usuário precisa ter no mínimo 3 caracteres!')
        return render(request, 'usuarios/register.html')

    if len(senha) < 6:
        messages.error(request, 'Senha muito curta. Digite  6 caracteres ou mais!')
        return render(request, 'usuarios/register.html')

    if senha != repsenha:
        messages.error(request, 'As senhas precisam ser iguais!')
        return render(request, 'usuarios/register.html')

    if User.objects.filter(username=user).exists():
        messages.error(request, 'Este usuário já existe!')
        return render(request, 'usuarios/register.html')

    if User.objects.filter(email=email).exists():
        messages.error(request, 'Este e-mail já está cadastrado!')
        return render(request, 'usuarios/register.html')

    messages.success(request, 'Registro realizado com sucesso! Agora faça seu login.')
    user = User.objects.create_user(username=user, email=email, password=senha, first_name=nome, last_name=sobrenome)
    user.save()
    return redirect('login')


@login_required(login_url='login')
def dashboard(request):
    if request.method != 'POST':
        form = FormContato
        return render(request, 'usuarios/dashboard.html', {'form': form})

    form = FormContato(request.POST, request.FILES)

    if not form.is_valid():
        messages.error(request, 'Erro ao enviar formulário.')
        form = FormContato(request.POST)
        return render(request, 'usuarios/dashboard.html', {'form': form})

    #descricao = request.POST.get('descricao')

    form.save()
    messages.success(request, f'Contato {request.POST.get("nome")} salvo com sucesso!')
    return redirect('dashboard')
