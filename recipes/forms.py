from django import forms


class RecipeAdd(forms.Form):
    def __init__(self, user, *args, **kwargs):
        super(RecipeAdd, self).__init__(*args, **kwargs)
        self.fields['author'].choices = [(user.author.id, user.author.name)]
    name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    time_required = forms.CharField(max_length=50)
    instructions = forms.CharField(widget=forms.Textarea)
    author = forms.ChoiceField()


class SignupForm(forms.Form):
    username = forms.CharField(max_length=50)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    name = forms.CharField(max_length=50)
    bio = forms.CharField(widget=forms.Textarea)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())
