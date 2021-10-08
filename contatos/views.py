from django.shortcuts import render, get_object_or_404, redirect
from .models import Contato
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def index(request):
    try:

        contatos = Contato.objects.order_by('id').filter(
            mostrar=True
        )

        ### criando a paginação
        paginator = Paginator(contatos, 10)
        page = request.GET.get('p')
        contatos = paginator.get_page(page)

        # try:
        #     contatos = paginator.page(page)
        # except PageNotAnInteger:
        #     contatos = paginator.page(1)
        # except EmptyPage:
        #     contatos = paginator.page(paginator.num_pages)

        return render(request, 'contatos/index.html', {
            'contatos': contatos
        })
    except Contato.DoesNotExist as e:
        return render(request, 'contatos/404.html')


@login_required(login_url='login')
def pg_contato(request, contato_id):
    try:
        contato = Contato.objects.get(id=contato_id)
        # contato = get_object_or_404(Contato, id=contato_id)

        if not contato.mostrar:
            return render(request, 'contatos/404.html')
        else:
            return render(request, 'contatos/pg_contato.html', {
                'contato': contato
            })
    except Contato.DoesNotExist as e:
        return render(request, 'contatos/404.html')


@login_required(login_url='login')
def busca(request):
    try:
        ### pegando valor da pagina
        termo = request.GET.get('termo')

        ### Evitar busca sem termo (<> termo vazio)
        if termo is None or not termo:
            messages.add_message(request, messages.ERROR, 'O campo de busca não pode ficar vazio.')
            return redirect('index')

        campos = Concat('nome', Value(' '), 'sobrenome')

        contatos = Contato.objects.annotate(
            nome_completo=campos).filter(
            nome_completo__icontains=termo
        )


        ### ver a query: print(contatos.query)

        ### criando a paginação
        paginator = Paginator(contatos, 10)
        page = request.GET.get('p')
        contatos = paginator.get_page(page)

        return render(request, 'contatos/busca.html', {
            'contatos': contatos
        })
    except Contato.DoesNotExist as e:
        return render(request, 'contatos/404.html')
