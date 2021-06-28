from django.shortcuts import render, redirect
from .models import Recipe, Category, Country, Recommendation, IngredientsRecipe, Rating, TypeIngredient, Ingredients, Dictionary, EquipmentTips
from .form import RecommendationForm, RecipeForm
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.core import serializers
from django.views.generic.detail import DetailView



def dashboard_with_pivot(request):
    return render(request, 'main/dashboard_with_pivot.html', {})


def pivot_data(request):
    dataset = Ingredients.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)


def index(request):
    recipe1 = Recipe.objects.all()[:6]
    recipe2 = Recipe.objects.order_by("-CreateDate")[:9]
    recipe3 = Recipe.objects.filter(rating__Rating="5")
    recipe4 = Rating.objects.all()
    recipe5 = Recipe.objects.all().count()
    recipe = {"recipe1": recipe1, "recipe2": recipe2, "recipe3": recipe3, "recipe4": recipe4, "recipe5": recipe5,
              "recipe": Recipe.objects.all()}
    return render(request, 'main/index.html', recipe)


def category(request):
    category = Category.objects.all()
    return render(request, 'main/category.html', {'category': category})


class categorycardDetailView(DetailView):
    model = Category
    context_object_name = 'category'
    template_name = 'main/categorycard.html'

    def get_context_data(self, **kwargs):
        context = super(categorycardDetailView, self).get_context_data(**kwargs)
        context['test'] = Recipe.objects.all()
        return context


class cardDetailView(DetailView):
    model = Recipe
    context_object_name = 'recipe'
    template_name = 'main/card.html'

    def get_context_data(self, **kwargs):
        context = super(cardDetailView, self).get_context_data(**kwargs)
        context['test'] = Ingredients.objects.all()
        return context


def recom(request):
    recomendation = Recommendation.objects.all()
    return render(request, 'main/recomendation.html', {'recomendation': recomendation})


def dictionary(request):
    dictionary = Dictionary.objects.all()
    return render(request, 'main/dictionary.html', {'dictionary': dictionary})


def tablepr(request):
    tablepr1 = TypeIngredient.objects.all()
    tablepr2 = Ingredients.objects.all()
    tableproduct = {"tablepr1": tablepr1, "tablepr2": tablepr2}
    return render(request, 'main/tableproduct.html', tableproduct)


def createrecom(request):
    error = ''
    if request.method == 'POST':
        form = RecommendationForm(request.POST, request.FILES)
        if form.is_valid():
            thought = form.save(commit=False)
            thought.Userid = User.objects.get(pk=request.user.id)
            thought.save()
            redirect('recomendation/')
        else:
            error = 'Форма была неверной'

    form = RecommendationForm()
    createrecom = {
        'form': form,
        'error': error
    }
    return render(request, 'main/createrecom.html', createrecom)


def createrecipe(request):
    error = ''
    country1 = Country.objects.all()[:20]
    country2 = Country.objects.all()[20:40]
    country3 = Country.objects.all()[40:60]
    country4 = Country.objects.all()[60:80]
    if request.method == 'POST':
        form1 = RecipeForm(request.POST, request.FILES)
        if form1.is_valid():
            thought = form1.save(commit=False)
            thought.Userid = User.objects.get(pk=request.user.id)
            thought.save()
            redirect('createrecipe/')
        else:
            error = 'Форма была неверной'

    form1 = RecipeForm()
    createrecipe = {
        'form1': form1,
        'error': error,
        'country1': country1,
        'country2': country2,
        'country3': country3,
        'country4': country4
    }
    return render(request, 'main/createrecipe.html', createrecipe)


def equipmentTips(request):
    equipmentTips = EquipmentTips.objects.all()
    return render(request, 'main/equipmentTips.html', {'equipmentTips': equipmentTips})
