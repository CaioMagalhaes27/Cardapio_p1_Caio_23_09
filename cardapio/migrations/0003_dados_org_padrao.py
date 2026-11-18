from django.db import migrations


def popular_org_padrao(apps, schema_editor):
    Organizacao = apps.get_model('cardapio', 'Organizacao')
    org, _ = Organizacao.objects.get_or_create(nome='Restaurante Padrão (P1)')

    for model_name in ['Categoria', 'Produto', 'Mesa', 'Pedido', 'ItemPedido']:
        Model = apps.get_model('cardapio', model_name)
        Model.objects.filter(organizacao__isnull=True).update(organizacao=org)


class Migration(migrations.Migration):

    dependencies = [
        ('cardapio', '0002_add_organizacao_nullable'),  # <-- Mantenha o nome exato que já estava aqui!
    ]

    operations = [
        migrations.RunPython(popular_org_padrao, migrations.RunPython.noop),
    ]