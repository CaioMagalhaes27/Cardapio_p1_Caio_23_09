from django.contrib import admin
from .models import Organizacao, Perfil, Categoria, Produto, Mesa, Pedido, ItemPedido


@admin.register(Organizacao)
class OrganizacaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'criada_em')


@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'organizacao')
    list_filter = ('organizacao',)


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'organizacao', 'ativo')
    list_filter = ('organizacao',)


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'preco', 'organizacao', 'disponivel')
    list_filter = ('organizacao', 'categoria')


@admin.register(Mesa)
class MesaAdmin(admin.ModelAdmin):
    list_display = ('numero', 'status', 'organizacao')
    list_filter = ('organizacao',)


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'mesa', 'status', 'organizacao', 'data_criacao')
    list_filter = ('organizacao', 'status')


@admin.register(ItemPedido)
class ItemPedidoAdmin(admin.ModelAdmin):
    list_display = ('pedido', 'produto', 'quantidade', 'preco_unitario', 'organizacao')
    list_filter = ('organizacao',)