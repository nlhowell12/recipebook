from django import forms
from .models import Author

class RecipeAdd(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    time_required = forms.CharField(max_length=50)
    instructions = forms.CharField(widget=forms.Textarea)
    authors = [(a.id, a.name) for a in Author.objects.all()]
    author = forms.ChoiceField(choices=authors)