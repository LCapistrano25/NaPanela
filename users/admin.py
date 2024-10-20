from django.contrib import admin

from core.mixins import SaveModelMixin
from users.models import User

class UserAdmin(SaveModelMixin, admin.ModelAdmin):
    list_display = ['first_name', 'email']
    search_fields = ['first_name', 'email']
    list_per_page = 10

    fieldsets = (
        (None, {
            'fields': ('first_name', 'email', 'password', 'is_active', 'is_staff', 'is_superuser')
        }),
    )

admin.site.register(User, UserAdmin)