from django.shortcuts import render, get_object_or_404
from .models import Contato
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    try:
        contatos = Contato.objects.all().order_by('id')

        ### criando a paginação
        paginator = Paginator(contatos, 10)
        page = request.GET.get('p', 1)
        #contatos = paginator.get_page(page)

        try:
            contatos = paginator.page(page)
        except PageNotAnInteger:
            contatos = paginator.page(1)
        except EmptyPage:
            contatos = paginator.page(paginator.num_pages)

        return render(request, 'contatos/index.html', {
            'contatos': contatos
        })
    except Contato.DoesNotExist as e:
        return render(request, 'contatos/404.html')


def pg_contato(request, contato_id):
    try:
        contato = Contato.objects.get(id = contato_id)
        #contato = get_object_or_404(Contato, id=contato_id)
        return render(request, 'contatos/pg_contato.html', {
            'contato': contato
        })
    except Contato.DoesNotExist as e:
        return render(request, 'contatos/404.html')