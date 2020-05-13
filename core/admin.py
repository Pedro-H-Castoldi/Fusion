from django.contrib import admin
from .models import Cargo, Servico, Funcionario, Features

@admin.register(Cargo)
class CardoAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'ativo', 'modificado')

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('servico', 'ativo', 'modificado')

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'ativo', 'modificado')

@admin.register(Features)
class FeaturesAdmin(admin.ModelAdmin):
    list_display = ('recurso', 'ativo', 'modificado')
