from .models import Recommendation
from django.forms import ModelForm, TextInput, Textarea
from django.contrib.auth.models import User


class RecommendationForm(ModelForm):
    class Meta:
        model = Recommendation
        fields = ["Name", "Instruction", "Img", "Userid"]
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

