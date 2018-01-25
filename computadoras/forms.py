from django import forms
from .models import ComputadoraModel


class ComputadoraForm(forms.ModelForm):
    class Meta:
        model = ComputadoraModel
        fields = '__all__'