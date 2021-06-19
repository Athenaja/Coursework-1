from django.contrib import admin
from .models import Recipe, Ingredients, Category, Country, RecipeUser, Recommendation, RecommendationUser, Rating

admin.site.register(Recipe)
admin.site.register(Ingredients)
admin.site.register(Category)
admin.site.register(Country)
admin.site.register(RecipeUser)
admin.site.register(Recommendation)
admin.site.register(RecommendationUser)
admin.site.register(Rating)


