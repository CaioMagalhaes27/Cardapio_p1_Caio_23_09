from rest_framework import serializers
from .models import Categoria, Produto, Mesa, Pedido, ItemPedido


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nome', 'descricao', 'ativo']


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['id', 'categoria', 'nome', 'descricao', 'preco', 'disponivel']

    def validate_preco(self, value):
        if value <= 0:
            raise serializers.ValidationError("O preço do produto deve ser maior que zero.")
        return value


class MesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mesa
        fields = ['id', 'numero', 'status']


class ItemPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemPedido
        fields = ['id', 'pedido', 'produto', 'quantidade', 'preco_unitario']

    def validate_quantidade(self, value):
        if value <= 0:
            raise serializers.ValidationError("A quantidade deve ser de pelo menos 1 unidade.")
        return value

    def validate_preco_unitario(self, value):
        if value <= 0:
            raise serializers.ValidationError("O preço unitário deve ser maior que zero.")
        return value


class PedidoSerializer(serializers.ModelSerializer):
    itens = ItemPedidoSerializer(many=True, read_only=True)

    class Meta:
        model = Pedido
        fields = ['id', 'mesa', 'data_criacao', 'status', 'itens']
        read_only_fields = ['data_criacao']