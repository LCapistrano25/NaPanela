from rest_framework.serializers import ModelSerializer
from core.mixins import SaveSerializerMixin
from recipes.models import Recipe, UserRecipe

class RecipeModelSerializer(SaveSerializerMixin, ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['id', 'name', 'image', 'ingredients', 'preparation', 'category_id', 'country_id', 
                  'status', 'created_by_name', 'created_at', 'updated_by_name', 'updated_at']

class UserRecipeModelSerializer(SaveSerializerMixin, ModelSerializer):
    class Meta:
        model = UserRecipe
        fields = ['id', 'user_id', 'recipe_id', 'status', 'created_by_name', 'created_at', 
                  'updated_by_name', 'updated_at']