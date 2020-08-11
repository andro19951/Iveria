"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from .models import Recipe, Ingredients, Categories, Cattorec, Ingtorec

def home(request):
    """Renders the home page."""
    categories = Categories.objects.all()
    recipes = Recipe.objects.all()[:5]

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home',
            'categories': categories,
            'recipes': recipes,
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
def category(request, category):
    categories = Categories.objects.all()
    recipeids = Cattorec.objects.filter(Category_id=category)
    rec=[]
    for recipeid in recipeids:
        rec.append(Recipe.objects.get(Title=recipeid.Recipe_id))

    return render(request, "app/category.html",{
        'categoriID': Categories.objects.get(pk=category),
        'categories': categories,
        'recipes': rec,
        })

def recipe(request, recipe_id):
    categories = Categories.objects.all()
    recipe = Recipe.objects.get(pk=recipe_id)
    Ingredientids = Ingtorec.objects.filter(Recipe_id=recipe_id)
    ing=[]
    for Ingredientid in Ingredientids:
        ing.append(Ingredients.objects.get(Ingredient=Ingredientid.Ingredient_id))
    return render(request, "app/recipe.html",{
        'categories': categories,
        'Ingredients': ing,
        'recipe': recipe,
        
        })