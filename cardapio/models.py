from django.db import models
from django.contrib.auth.models import User


class Organizacao(models.Model):
    nome = models.CharField(max_length=120)
    criada_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


class DaOrganizacao(models.Model):
    organizacao = models.ForeignKey(
        Organizacao,
        on_delete=models.PROTECT,
    )

    class Meta:
        abstract = True


class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    organizacao = models.ForeignKey(Organizacao, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.usuario.username} - {self.organizacao.nome}"


class Categoria(DaOrganizacao):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome


class Produto(DaOrganizacao):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='produtos')
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return self.nome


class Mesa(DaOrganizacao):
    numero = models.IntegerField()
    status = models.CharField(max_length=20, default='Livre')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['organizacao', 'numero'],
                name='mesa_unica_por_org',
            )
        ]

    def __str__(self):
        return f"Mesa {self.numero}"


class Pedido(DaOrganizacao):
    STATUS_CHOICES = [
        ('Pendente', 'Pendente'),
        ('Em Preparo', 'Em Preparo'),
        ('Entregue', 'Entregue'),
        ('Cancelado', 'Cancelado'),
    ]
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)
    data_criacao = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pendente')

    def __str__(self):
        return f"Pedido #{self.id} - Mesa {self.mesa.numero}"


class ItemPedido(DaOrganizacao):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantidade}x {self.produto.nome}"