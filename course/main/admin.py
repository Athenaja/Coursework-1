from django.contrib import admin
from .models import Recipe, Ingredients, Category, Country, RecipeUser, Recommendation, Rating, RecipeCategory, IngredientsRecipe, TypeIngredient, Dictionary, EquipmentTips

admin.site.register(Recipe)
admin.site.register(RecipeCategory)
admin.site.register(IngredientsRecipe)
admin.site.register(Ingredients)
admin.site.register(Category)
admin.site.register(Country)
admin.site.register(RecipeUser)
admin.site.register(Recommendation)
admin.site.register(Rating)
admin.site.register(TypeIngredient)
admin.site.register(Dictionary)
admin.site.register(EquipmentTips)


