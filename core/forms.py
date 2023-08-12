from django import forms
from core.models import Film


class FilmForm(forms.ModelForm):
    class Meta:
        model = Film 
        fields = ('name', 'director')