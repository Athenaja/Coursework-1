from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Recipe, Category, Country, Recommendation
from .form import RecommendationForm


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


def recom(request):
    recomendation = Recommendation.objects.all()
    return render(request, 'main/recomendation.html', {'recomendation': recomendation})


def createrecom(request):
    error = ''
    if request.method == 'POST':
        form = RecommendationForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('recomendation/')
        else:
            error = 'Форма была неверной'

    form = RecommendationForm()
    createrecom = {
        'form': form,
        'error': error
    }
    return render(request, 'main/createrecom.html', createrecom)
