from .models import Recommendation
from django.forms import ModelForm, TextInput, Textarea


class RecommendationForm(ModelForm):
    class Meta:
        model = Recommendation
        fields = ["Name", "Instruction", "Img"]
        widgets = {
            "Name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название совета'
            }),
            "Instruction": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите совет'
            }),
        }

