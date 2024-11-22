import django_filters

from .models import Recipe, UserRecipe

class RecipeFilter(django_filters.FilterSet):
    user_id = django_filters.CharFilter(method='filter_user_id')  # Atualizado para o método correto
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Recipe
        fields = ['user_id', 'name']

    def filter_user_id(self, queryset, name, value):
        return queryset.filter(id__in=UserRecipe.objects.filter(user_id=value).values_list('recipe_id', flat=True))


class UserRecipeFilter(django_filters.FilterSet):
    user_id = django_filters.CharFilter(field_name='user_id', lookup_expr='exact')
    recipe_id = django_filters.CharFilter(field_name='recipe_id', lookup_expr='exact')

    name = django_filters.CharFilter(field_name='recipe_id__name', lookup_expr='icontains')

    class Meta:
        model = UserRecipe
        fields = ['user_id', 'recipe_id', 'name']