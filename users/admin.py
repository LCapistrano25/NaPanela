from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from users.models import User
from core.mixins import SaveModelMixin

class UserAdmin(SaveModelMixin, BaseUserAdmin):
    # Campos exibidos na lista de usuários
    list_display = [
        'id', 'username', 'first_name', 'last_name', 'email',
        'is_active', 'is_staff', 'is_superuser', 'last_login', 'date_joined'
    ]
    search_fields = ['username', 'first_name', 'last_name', 'email']
    list_filter = ['is_staff', 'is_superuser', 'is_active']
    list_per_page = 10

    # Configuração dos campos no formulário de edição
    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Informações Pessoais', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissões', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
            'classes': ('collapse',),
        }),
        ('Datas Importantes', {
            'fields': ('last_login', 'date_joined')
        }),
    )

    # Filtros horizontais para grupos e permissões
    filter_horizontal = ('groups', 'user_permissions')

    # Formulário de adição de novo usuário
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
    )

    readonly_fields = ['last_login', 'date_joined']
    
# Registra o modelo User com a customização
admin.site.register(User, UserAdmin)

# Remove o modelo Group do admin caso não seja necessário individualmente
admin.site.unregister(Group)
