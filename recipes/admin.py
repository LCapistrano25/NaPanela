from django.contrib import admin
from recipes.models import Recipe, UserRecipe
from core.mixins import SaveModelMixin

class RecipeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category_id', 'country_id', 'status', 
                    'created_by', 'created_at', 'updated_by', 'updated_at']
    search_fields = ['name', 'category_id', 'country_id']
    list_filter = ['status', 'created_at', 'updated_at']
    
    fieldsets = (
        (None, {
            'fields': ('name', 'image', 'description', 'ingredients', 'preparation', 'category_id', 'country_id', 'status')
        }),
        ('Control', {
            'fields': ('created_by', 'created_at', 'updated_by', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    readonly_fields = ['created_by', 'created_at', 'updated_by', 'updated_at']


class UserRecipeAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_id', 'recipe_id', 'status', 'created_by', 
                    'created_at', 'updated_by', 'updated_at']
    search_fields = ['user_id', 'recipe_id']
    list_filter = ['status', 'created_at', 'updated_at']
    
    fieldsets = (
        (None, {
            'fields': ('user_id', 'recipe_id', 'status')
        }),
        ('Control', {
            'fields': ('created_by', 'created_at', 'updated_by', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    readonly_fields = ['created_by', 'created_at', 'updated_by', 'updated_at']

admin.site.register(Recipe, RecipeAdmin)  
admin.site.register(UserRecipe, UserRecipeAdmin)