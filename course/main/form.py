from .models import Recommendation
from django.forms import ModelForm


class RecommendationForm(ModelForm):
    class Meta:
        model = Recommendation
        fields = ["Name", "Instruction", "Img"]