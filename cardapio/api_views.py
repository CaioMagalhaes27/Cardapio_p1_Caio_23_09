from rest_framework import generics
from .models import Categoria, Produto, Mesa, Pedido, ItemPedido
from .serializers import (
    CategoriaSerializer,
    ProdutoSerializer,
    MesaSerializer,
    PedidoSerializer,
    ItemPedidoSerializer,
)


# --- CATEGORIAS ---
class CategoriaListCreate(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class CategoriaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


# --- PRODUTOS ---
class ProdutoListCreate(generics.ListCreateAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


class ProdutoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


# --- MESAS ---
class MesaListCreate(generics.ListCreateAPIView):
    queryset = Mesa.objects.all()
    serializer_class = MesaSerializer


class MesaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mesa.objects.all()
    serializer_class = MesaSerializer


# --- PEDIDOS ---
class PedidoListCreate(generics.ListCreateAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer


class PedidoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer


# --- ITENS DO PEDIDO ---
class ItemPedidoListCreate(generics.ListCreateAPIView):
    queryset = ItemPedido.objects.all()
    serializer_class = ItemPedidoSerializer


class ItemPedidoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ItemPedido.objects.all()
    serializer_class = ItemPedidoSerializer