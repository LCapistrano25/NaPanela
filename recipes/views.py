from datetime import datetime
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from recipes.models import Recipe, UserRecipe, WeeklyRecipe
from recipes.serializers import RecipeModelSerializer, UserRecipeModelSerializer

from recipes.filters import RecipeFilter, UserRecipeFilter

from recipes.utils import get_recipe, random_recipe, create_weekly_recipe

class RecipeListCreateAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Recipe.objects.all()
    serializer_class = RecipeModelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = RecipeFilter

class RecipeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Recipe.objects.all()
    serializer_class = RecipeModelSerializer

class UserRecipeListCreateAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = UserRecipe.objects.all()
    serializer_class = UserRecipeModelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserRecipeFilter

class UserRecipeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = UserRecipe.objects.all()
    serializer_class = UserRecipeModelSerializer

class RandomRecipeListAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Recipe.objects.all()
    serializer_class = RecipeModelSerializer

    def get_queryset(self):
        weekly_recipe = WeeklyRecipe.objects.filter(
            user_id=self.request.user,
            week=datetime.now().isocalendar()[1],
            month=datetime.now().month,
            year=datetime.now().year
        )

        if weekly_recipe.exists():
            return Recipe.objects.filter(id__in=weekly_recipe.values_list('recipe_id', flat=True))

        recipes = get_recipe()
        recipes_random = random_recipe(recipes)

        print(recipes_random)
        for recipe in recipes_random:
            recipe_created = create_weekly_recipe(user_id=self.request.user, recipe_id=recipe)
            print(recipe_created)
        return recipes_random