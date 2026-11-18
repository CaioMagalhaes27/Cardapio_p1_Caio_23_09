from django.urls import path
from .api_views import (
    CategoriaListCreate, CategoriaDetail,
    ProdutoListCreate, ProdutoDetail,
    MesaListCreate, MesaDetail,
    PedidoListCreate, PedidoDetail,
    ItemPedidoListCreate, ItemPedidoDetail,
)

urlpatterns = [
    path('categorias/', CategoriaListCreate.as_view(), name='api_categoria_list'),
    path('categorias/<int:pk>/', CategoriaDetail.as_view(), name='api_categoria_detail'),

    path('produtos/', ProdutoListCreate.as_view(), name='api_produto_list'),
    path('produtos/<int:pk>/', ProdutoDetail.as_view(), name='api_produto_detail'),

    path('mesas/', MesaListCreate.as_view(), name='api_mesa_list'),
    path('mesas/<int:pk>/', MesaDetail.as_view(), name='api_mesa_detail'),

    path('pedidos/', PedidoListCreate.as_view(), name='api_pedido_list'),
    path('pedidos/<int:pk>/', PedidoDetail.as_view(), name='api_pedido_detail'),

    path('itens-pedido/', ItemPedidoListCreate.as_view(), name='api_item_pedido_list'),
    path('itens-pedido/<int:pk>/', ItemPedidoDetail.as_view(), name='api_item_pedido_detail'),
]