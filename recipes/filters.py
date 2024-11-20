import django_filters

from .models import Recipe, UserRecipe

class RecipeFilter(django_filters.FilterSet):
    user_id = django_filters.CharFilter(method='filter_user_id')  # Atualizado para o método correto

    class Meta:
        model = Recipe
        fields = ['name', 'description']

    def filter_user_id(self, queryset, name, value):
        return queryset.filter(id__in=UserRecipe.objects.filter(user_id=value).values_list('recipe_id', flat=True))


class UserRecipeFilter(django_filters.FilterSet):
    user_id = django_filters.CharFilter(field_name='user_id', lookup_expr='exact')
    recipe_id = django_filters.CharFilter(field_name='recipe_id', lookup_expr='exact')
                                          
    class Meta:
        model = UserRecipe
        fields = ['user_id', 'recipe_id']