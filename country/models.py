from django.db import models
from core.models import BaseModel

class Country(BaseModel):
    name = models.CharField(
        max_length=255, 
        db_column='nome', 
        verbose_name='Nome'
    )

    initials = models.CharField(
        max_length=5, 
        db_column='sigla', 
        verbose_name='Sigla'
    )

    status = models.BooleanField(
        default=True, 
        db_column='status', 
        verbose_name='Status'
    )
    
    class Meta:
        db_table = 'tb_pais'
        verbose_name = 'País'
        verbose_name_plural = 'Países'

    def __str__(self):
        return self.name