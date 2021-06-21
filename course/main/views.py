from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe, Category, Country


def index(request):
    recipe = Recipe.objects.all()[:6]
    # recipedata = Recipe.objects.get(Name='Кимпаб')
    # recipedata = Recipe.objects.order_by("-CreateDate")
    return render(request, 'main/index.html', {'recipe': recipe})


def category(request):
    category = Category.objects.all()
    return render(request, 'main/category.html', {'category': category})


def card(request):
    country = Country.objects.all()
    return render(request, 'main/card.html', {'country': country})
