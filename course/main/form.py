from .models import Recommendation, Recipe
from django.forms import ModelForm, TextInput, Textarea
from django.contrib.auth.models import User


class RecommendationForm(ModelForm):

    class Meta:
        model = Recommendation
        fields = ["Name", "Instruction", "Img"]
        widgets = {
            "Name": TextInput(attrs={
                'class': 'form-control ml-100 mr-100',
                'placeholder': 'Введите название совета'
            }),
            "Instruction": Textarea(attrs={
                'class': 'form-control ml-100 mr-100',
                'placeholder': 'Введите совет'
            }),
        }


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ["Name", "Instruction", "Img", "CountryID"]
        widgets = {
            "Name": TextInput(attrs={
                'class': 'form-control ml-100 mr-100',
                'placeholder': 'Введите название рецепта'
            }),
            "Instruction": Textarea(attrs={
                'class': 'form-control ml-100 mr-100',
                'placeholder': 'Введите рецепт'
            }),
            "CountryID": TextInput(attrs={
                'class': 'form-control ml-100 mr-100',
                'placeholder': 'Введите ID страны'
            }),
        }

