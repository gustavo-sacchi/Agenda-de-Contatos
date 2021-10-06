from django.contrib import admin
from .models import Categoria, Contato


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'telefone', 'email', 'categoria', 'categoria_especial', 'mostrar')
    list_display_links = ('id', 'nome', 'sobrenome')
    list_filter = ('categoria_especial', 'categoria')
    list_per_page = 20
    list_editable = ('telefone', 'categoria_especial', 'mostrar')


admin.site.register(Contato, ContatoAdmin)
admin.site.register(Categoria)