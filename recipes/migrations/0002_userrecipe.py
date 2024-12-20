# Generated by Django 5.1.2 on 2024-10-20 15:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRecipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='criado_em', verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, db_column='atualizado_em', verbose_name='Atualizado em')),
                ('status', models.BooleanField(db_column='status', default=True, verbose_name='Status')),
                ('created_by', models.ForeignKey(blank=True, db_column='id_criado_por', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_created', to=settings.AUTH_USER_MODEL, verbose_name='Criado por')),
                ('recipe_id', models.ForeignKey(db_column='id_receita', on_delete=django.db.models.deletion.CASCADE, to='recipes.recipe', verbose_name='Receita')),
                ('updated_by', models.ForeignKey(blank=True, db_column='id_atualizado_por', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_updated', to=settings.AUTH_USER_MODEL, verbose_name='Atualizado por')),
                ('user_id', models.ForeignKey(db_column='id_usuario', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Usuário Receita',
                'verbose_name_plural': 'Usuários Receitas',
                'db_table': 'tb_usuario_receita',
            },
        ),
    ]
