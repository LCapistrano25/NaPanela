from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    number = models.CharField(max_length=255, db_column='numero', verbose_name='Número')

    class Meta:
        db_table = 'tb_usuario'
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return self.username
