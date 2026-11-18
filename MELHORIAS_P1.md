# 🔧 Melhorias e Dívida Técnica - Pós-P1 (Cardápio Digital)

Pontos identificados na entrega da P1 que serão refatorados para a evolução da API e da P2:

1. **Centralizar Validação de Negócio nos Models (`clean()`):**
   - Na P1, a validação de preço (`preco > 0`) ficou restrita à view/formulário. Mover essa regra para o método `clean()` do model `Produto` (e validar `quantidade > 0` / `preco_unitario > 0` em `ItemPedido`) garante integridade também no Django Admin e na API REST.

2. **Preenchimento Automático de `preco_unitario` em `ItemPedido`:**
   - Atualmente `preco_unitario` precisa ser informado manualmente na criação do `ItemPedido`. O ideal é sobrescrever o `save()` ou tratar no serializer/view para capturar automaticamente o `produto.preco` vigente no momento do pedido, evitando divergências de valor.

3. **Controle Automático de Status da `Mesa`:**
   - Ao abrir um novo `Pedido` com status `Pendente` ou `Em Preparo`, o status da `Mesa` deveria atualizar automaticamente de `'Livre'` para `'Ocupada'` (e retornar para `'Livre'` quando o pedido for `'Entregue'` ou `'Cancelado'`).

4. **Uso de `ModelForm` e `.gitignore` no Repositório:**
   - Refatorar views que manipulam `request.POST` manualmente para `ModelForm` e adicionar um `.gitignore` padrão Django para parar de versionar arquivos de cache (`__pycache__/`).