from django.contrib import admin
from core.mixins import SaveModelMixin
from categories.models import Category

class CategoryAdmin(SaveModelMixin, admin.ModelAdmin):
    list_display = ['name', 'created_by', 'created_at', 'updated_by', 'updated_at']
    search_fields = ['name']
    list_filter = ['created_at', 'updated_at']
    list_per_page = 10

    fieldsets = ( 
        (None, {
            'fields': ('name', 'status')
        }),

        ('control', {
            'classes': ('collapse',),
            'fields': ('created_by', 'created_at', 'updated_by', 'updated_at')
        })
    )

    readonly_fields = ('created_by', 'created_at', 'updated_by', 'updated_at')
    
admin.site.register(Category, CategoryAdmin)