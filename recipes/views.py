from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from recipes.models import Recipe, UserRecipe
from recipes.serializers import RecipeModelSerializer, UserRecipeModelSerializer

from recipes.filters import RecipeFilter, UserRecipeFilter

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
    