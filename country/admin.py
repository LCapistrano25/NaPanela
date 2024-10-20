from django.contrib import admin
from core.mixins import SaveModelMixin
from country.models import Country

class CountryAdmin(SaveModelMixin, admin.ModelAdmin):
    list_display = ['name', 'initials', 'created_by', 'created_at', 'updated_by', 'updated_at']
    search_fields = ['name']
    list_filter = ['created_at', 'updated_at']
    list_per_page = 10

    fieldsets = (
        (None, {
            'fields': ('name', 'initials', 'status')
        }),

        ('control', {
            'classes': ('collapse',),
            'fields': ('created_by', 'created_at', 'updated_by', 'updated_at')
        })
    )

    readonly_fields = ('created_by', 'created_at', 'updated_by', 'updated_at')

admin.site.register(Country, CountryAdmin)