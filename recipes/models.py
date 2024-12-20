from django.db import models

from core.models import BaseModel

from categories.models import Category
from country.models import Country
from users.models import User

class Recipe(BaseModel):
    name = models.CharField(
        max_length=255, 
        db_column='nome', 
        verbose_name='Nome'
    )

    image = models.URLField(
        db_column='imagem', 
        verbose_name='Imagem'
    )
    
    description = models.TextField(
        null=True,
        blank=True,
        db_column='descricao',
        verbose_name='Descrição'
    )
    ingredients = models.TextField(
        db_column='ingredientes', 
        verbose_name='Ingredientes'
    )

    preparation = models.TextField(
        db_column='preparacao', 
        verbose_name='Preparação'
    )

    category_id = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE, 
        db_column='id_categoria', 
        verbose_name='Categoria'
    )

    country_id = models.ForeignKey(
        Country, 
        on_delete=models.CASCADE, 
        db_column='id_pais', 
        verbose_name='País'
    )

    status = models.BooleanField(
        default=True, 
        db_column='status', 
        verbose_name='Status'
    )

    class Meta:
        db_table = 'tb_receita'
        verbose_name = 'Receita'
        verbose_name_plural = 'Receitas'

    def __str__(self):
        return self.name


class UserRecipe(BaseModel):
    user_id = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        db_column='id_usuario', 
        verbose_name='Usuário'
    )

    recipe_id = models.ForeignKey(
        Recipe, 
        on_delete=models.CASCADE, 
        db_column='id_receita', 
        verbose_name='Receita'
    )

    status = models.BooleanField(
        default=True, 
        db_column='status', 
        verbose_name='Status'
    )

    class Meta:
        db_table = 'tb_usuario_receita'
        verbose_name = 'Usuário Receita'
        verbose_name_plural = 'Usuários Receitas'

        unique_together = ['user_id', 'recipe_id']
    def __str__(self):
        return f'{self.user_id} - {self.recipe_id}'
    
class WeeklyRecipe(BaseModel):
    user_id = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        db_column='id_usuario', 
        verbose_name='Usuário'
    )

    recipe_id = models.ForeignKey(
        Recipe, 
        on_delete=models.CASCADE, 
        db_column='id_receita', 
        verbose_name='Receita'
    )

    week = models.IntegerField(
        db_column='semana', 
        verbose_name='Semana'
    )

    month = models.IntegerField(
        db_column='mes', 
        verbose_name='Mês'
    )

    year = models.IntegerField(
        db_column='ano', 
        verbose_name='Ano'
    )

    class Meta: 
        db_table = 'tb_semanal_receita'
        verbose_name = 'Semanal Receita'
        verbose_name_plural = 'Semanais Receitas'

        unique_together = ['user_id', 'recipe_id', 'week', 'month', 'year']