# 🍔 Cardápio Digital - Projeto P1

Sistema web desenvolvido em Django para gestão e consulta de um Cardápio Digital, criado como requisito de avaliação para a disciplina de **Laboratório de Programação Full Stack** da Universidade de Vassouras.

---

## 🚀 Tecnologias Utilizadas

- **Python 3.x**
- **Django 6.0+**
- **SQLite3**
- **Bootstrap 5** (com Bootstrap Icons)
- **Git / GitHub**

---

## 🛠️ Funcionalidades e Requisitos Cumpridos (P1)

### 1. Feature 1: Busca e Filtro na Listagem
- **Busca por texto:** Permite pesquisar pratos pelo nome usando o parâmetro `q` na URL.
- **Filtro por categoria:** Menu de seleção `<select>` para filtrar por categorias (Entradas, Pratos Principais, Sobremesas, Bebidas, etc.).
- **Busca Combinada `Q()`:** Utilização de objetos `Q` do Django ORM para aplicar busca por texto e filtro de categoria em simultâneo.
- **Persistência dos dados de busca:** Mantém o valor digitado no campo de texto após submeter o formulário.
- **Tratamento de resultados vazios:** Exibição de mensagem informativa via bloco `{% empty %}` quando nenhum item corresponde aos filtros.

### 2. Feature 2: Validação Customizada
- **Regra de Negócio:** Validação no cadastro para garantir que o **preço do prato seja maior que zero (`preco > 0`)**.
- **Tratamento de Erros:** Exibição de alertas visuais na interface caso o utilizador tente registar um preço inválido, nulo ou negativo.

---

## 📝 Relatório da Entrega P1

### Justificativa das Features (Cardápio Digital)
Para a **Feature 1**, foi escolhido o campo de texto `nome` para busca e o relacionamento `categoria` para a filtragem por tipo de item. Esta escolha permite aos clientes encontrar rapidamente um prato específico ou navegar apenas pelas categorias desejadas (ex: Sobremesas, Bebidas).

Para a **Feature 2**, foi aplicada a regra de validação customizada no preço do prato, garantindo que nenhum item seja cadastrado com valor zero ou negativo (`preco > 0`). Sem essa validação, itens poderiam ser oferecidos gratuitamente ou gerar inconsistências no cálculo de pedidos e faturação da aplicação.

---

## ⚙️ Como Executar o Projeto Localmente

1. **Clonar o repositório:**
   ```bash
   git clone [https://github.com/CaioMagalhaes27/EXERCICIO_AULA_04_DJANGO_16_09.git](https://github.com/CaioMagalhaes27/EXERCICIO_AULA_04_DJANGO_16_09.git)
   cd EXERCICIO_AULA_04_DJANGO_16_09