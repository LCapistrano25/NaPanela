from django.urls import path
from recipes.views import (
    RecipeListCreateAPIView, 
    RecipeRetrieveUpdateDestroyAPIView, 
    UserRecipeListCreateAPIView, 
    UserRecipeRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    path(
        'recipes/', 
        RecipeListCreateAPIView.as_view(), 
        name='recipe-list-create'
    ),
    path(
        'recipes/<int:pk>/', 
        RecipeRetrieveUpdateDestroyAPIView.as_view(), 
        name='recipe-retrieve-update-destroy'
    ),
    
    path(
        'user-recipes/', 
        UserRecipeListCreateAPIView.as_view(), 
        name='user-recipe-list-create'
    ),
    path(
        'user-recipes/<int:pk>/', 
        UserRecipeRetrieveUpdateDestroyAPIView.as_view(), 
        name='user-recipe-retrieve-update-destroy'
    ),
]