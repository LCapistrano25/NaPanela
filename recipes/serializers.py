from core.mixins import SaveSerializerMixin
from recipes.models import Recipe, UserRecipe
from rest_framework import serializers

class RecipeModelSerializer(SaveSerializerMixin, serializers.ModelSerializer):

    name_country = serializers.CharField(source='country_id.name')
    name_category = serializers.CharField(source='category_id.name')
    favorite = serializers.SerializerMethodField()

    class Meta:
        model = Recipe
        fields = ['id', 'name', 'image', 'description', 'ingredients', 'preparation', 'name_category', 'category_id', 'name_country',      
                  'country_id', 'status', 'favorite', 'created_by_name', 'created_at', 'updated_by_name', 'updated_at']

    def get_favorite(self, obj):
        user = self.context.get('request').user
        if user.is_anonymous:
            return False
        return UserRecipe.objects.filter(user_id=user.id, recipe_id=obj.id, status=True).exists()
    
class UserRecipeModelSerializer(SaveSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = UserRecipe
        fields = ['id', 'user_id', 'recipe_id', 'status', 'created_by_name', 'created_at', 
                  'updated_by_name', 'updated_at']