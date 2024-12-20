# Generated by Django 5.1.2 on 2024-10-20 15:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='criado_em', verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, db_column='atualizado_em', verbose_name='Atualizado em')),
                ('name', models.CharField(db_column='nome', max_length=255, verbose_name='Nome')),
                ('initials', models.CharField(db_column='sigla', max_length=5, verbose_name='Sigla')),
                ('status', models.BooleanField(db_column='status', default=True, verbose_name='Status')),
                ('created_by', models.ForeignKey(blank=True, db_column='id_criado_por', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_created', to=settings.AUTH_USER_MODEL, verbose_name='Criado por')),
                ('updated_by', models.ForeignKey(blank=True, db_column='id_atualizado_por', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_updated', to=settings.AUTH_USER_MODEL, verbose_name='Atualizado por')),
            ],
            options={
                'verbose_name': 'País',
                'verbose_name_plural': 'Países',
                'db_table': 'tb_pais',
            },
        ),
    ]
