from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from recipes.models import Recipe, UserRecipe
from recipes.serializers import RecipeModelSerializer, UserRecipeModelSerializer


class RecipeListCreateAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Recipe.objects.all()
    serializer_class = RecipeModelSerializer

class RecipeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Recipe.objects.all()
    serializer_class = RecipeModelSerializer

class UserRecipeListCreateAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = UserRecipe.objects.all()
    serializer_class = UserRecipeModelSerializer

class UserRecipeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = UserRecipe.objects.all()
    serializer_class = UserRecipeModelSerializer
    