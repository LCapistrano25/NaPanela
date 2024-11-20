import random
from datetime import datetime
from recipes.models import Recipe, UserRecipe, WeeklyRecipe

def get_recipe(**kwargs):
    try:
        return Recipe.objects.filter(**kwargs)
    except Exception as e:
        return None
    
def random_recipe(recipes):
    try:
        return random.sample(list(recipes), 7)
    except Exception as e:
        print(e)

def create_weekly_recipe(user_id, recipe_id):
    try:

        week = get_week() 
        month = get_month()
        year = get_year()

        if not week or not month or not year:
            return None

        weekly_recipe = WeeklyRecipe(
            user_id=user_id,
            recipe_id=recipe_id,
            week=week,
            month=month,
            year=year
        )

        weekly_recipe.save()

        return weekly_recipe
    
    except Exception as e:
        print(e)
        return None

def get_month():
    try:
        return datetime.now().month
    except Exception as e:
        return None

def get_week():
    try:
        return datetime.now().isocalendar()[1]
    except Exception as e:
        return None

def get_year():
    try:
        return datetime.now().year
    except Exception as e:
        return None