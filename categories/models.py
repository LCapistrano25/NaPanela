from django.db import models
from core.models import BaseModel

class Category(BaseModel):
    name = models.CharField(
        max_length=255, 
        db_column='nome', 
        verbose_name='Nome'
    )

    status = models.BooleanField(
        default=True, 
        db_column='status', 
        verbose_name='Status'
    )
    
    class Meta:
        db_table = 'tb_categoria'
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.name