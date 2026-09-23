from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Produto, Categoria, Mesa, Pedido, ItemPedido

def home(request):
    produtos = Produto.objects.all()
    
    # Busca e Filtros
    q = request.GET.get('q', '')
    categoria_id = request.GET.get('categoria', '')

    filtros = Q()
    if q:
        filtros &= Q(nome__icontains=q)
    if categoria_id:
        filtros &= Q(categoria_id=categoria_id)

    produtos = produtos.filter(filtros)
    categorias = Categoria.objects.all()

    return render(request, 'cardapio/home.html', {
        'pratos': produtos,
        'categorias': categorias,
        'q': q,
        'categoria_id': categoria_id,
    })

def criar_prato(request):
    erro = None
    categorias = Categoria.objects.all()

    if request.method == 'POST':
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        preco = request.POST.get('preco')
        categoria_id = request.POST.get('categoria')

        try:
            preco_float = float(preco)
            if preco_float <= 0:
                erro = "O preço do produto deve ser maior que zero."
        except (ValueError, TypeError):
            erro = "Insira um valor numérico válido para o preço."

        if not erro:
            categoria = Categoria.objects.get(id=categoria_id)
            Produto.objects.create(
                nome=nome,
                descricao=descricao,
                preco=preco_float,
                categoria=categoria
            )
            return redirect('home')

    return render(request, 'cardapio/form_prato.html', {
        'categorias': categorias,
        'erro': erro
    })

def criar_pedido(request):
    produtos = Produto.objects.filter(disponivel=True)
    mesas = Mesa.objects.all()
    erro = None

    if request.method == 'POST':
        mesa_id = request.POST.get('mesa')
        produto_id = request.POST.get('produto')
        quantidade = request.POST.get('quantidade', 1)

        if not mesa_id or not produto_id:
            erro = "Por favor, selecione a mesa e o produto."
        else:
            try:
                qtd_int = int(quantidade)
                if qtd_int <= 0:
                    erro = "A quantidade deve ser pelo menos 1."
            except (ValueError, TypeError):
                erro = "Quantidade inválida."

        if not erro:
            mesa = get_object_or_404(Mesa, id=mesa_id)
            produto = get_object_or_404(Produto, id=produto_id)

            pedido = Pedido.objects.create(mesa=mesa)
            ItemPedido.objects.create(
                pedido=pedido,
                produto=produto,
                quantidade=qtd_int,
                preco_unitario=produto.preco
            )
            return redirect('home')

    return render(request, 'cardapio/form_pedido.html', {
        'produtos': produtos,
        'mesas': mesas,
        'erro': erro
    })