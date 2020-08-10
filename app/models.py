"""
Definition of models.
"""

from django.db import models

# Create your models here.
class Recipe(models.Model):
    Title = models.CharField(max_length=64)
    description = models.TextField()
    
    
    def __str__(self):
        return f"{self.Title}"

class Ingredients(models.Model):
    Ingredient = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.Ingredient}"

class Categories(models.Model):
    Category = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.Category}"

class Cattorec(models.Model):
    Category_id=models.ForeignKey(Categories, on_delete=models.CASCADE)
    Recipe_id=models.ForeignKey(Recipe, on_delete=models.CASCADE)

class Ingtorec(models.Model):
    Ingredient_id=models.ForeignKey(Ingredients, on_delete=models.CASCADE)
    Recipe_id=models.ForeignKey(Recipe, on_delete=models.CASCADE)

