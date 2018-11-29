from django import forms
from .models import Author

class RecipeAdd(forms.Form):
    def __init__(self, *args, **kwargs):
        super(RecipeAdd, self).__init__(*args, **kwargs)
        self.fields['author'].choices = get_author_list()
    name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    time_required = forms.CharField(max_length=50)
    instructions = forms.CharField(widget=forms.Textarea)
    author = forms.ChoiceField()

class AuthAdd(forms.Form):
    name = forms.CharField(max_length=50)
    bio = forms.CharField(widget=forms.Textarea)

def get_author_list():
    return [(a.id, a.name) for a in Author.objects.all()]
