
from django.contrib import admin
from .models import Categories, Ingredients, Recipe, Cattorec, Ingtorec

admin.site.register(Categories)
admin.site.register(Ingredients)
admin.site.register(Recipe)
admin.site.register(Cattorec)
admin.site.register(Ingtorec)