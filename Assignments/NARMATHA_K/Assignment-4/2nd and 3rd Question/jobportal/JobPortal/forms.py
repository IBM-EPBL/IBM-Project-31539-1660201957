from django.forms import ModelForm
from .models import *

class ApplyForm(ModelForm):
    class Meta:
        model=Candidates
        fields="__all__"