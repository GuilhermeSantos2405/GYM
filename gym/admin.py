from django.contrib import admin

from .models import Consultor, Home, Profissao, Suplementacao, Treinos


@admin.register(Consultor)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'sobrenome', 'profissao', 'preco',
                    'email', 'telefone', 'ativo']
    list_display_link = ['nome']


@admin.register(Profissao)
class ProfissaoAdmin(admin.ModelAdmin):
    list_display = ['id', 'profissao', ]


@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'descricao']
    list_display_link = ['nome']


@admin.register(Suplementacao)
class SuplementacaoAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'descricao']
    list_display_link = ['nome']


@admin.register(Treinos)
class TreinoscaoAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'descricao']
    list_display_link = ['nome']
