from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import reverse
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic.edit import UpdateView

from .models import Author, Recipe
from .forms import RecipeAdd, SignupForm, LoginForm


def index(request):
    recipe_list = Recipe.objects.all()
    context = {'recipe_list': recipe_list}

    return render(request, 'recipes/index.html', context)


def recipe_view(request, recipe_id):
    recipe_item = Recipe.objects.get(pk=recipe_id)

    context = {
        'recipe_item': recipe_item,
        'favorites': request.user.author.favorites.all()
    }
    return render(request, 'recipes/recipe_view.html', context)


def author_view(request, author_id):
    author_name = Author.objects.get(pk=author_id).name
    authors_recipes_object = Recipe.objects.filter(author__name=author_name)
    author_favorites = Author.objects.get(pk=author_id).favorites.all()
    authors_recipes = []
    for recipe in authors_recipes_object:
        authors_recipes.append(recipe)
    context = {
        'author_name': author_name,
        'authors_recipes': authors_recipes,
        'author_favorites': author_favorites
    }
    return render(request, 'authors/author_view.html', context)

# Login required checks to see which, if any, user is logged in


@login_required()
def recipe_add(request):
    html = 'recipes/recipe_add.html'
    form = None

    if request.method == 'POST':
        form = RecipeAdd(request.user, request.POST)
        if form.is_valid():
            data = form.cleaned_data

            Recipe.objects.create(
                name=data['name'],
                description=data['description'],
                time_required=data['time_required'],
                instructions=data['instructions'],
                author=Author.objects.get(id=data['author'])
            )
        return render(request, 'recipes/thanks.html')
    else:
        form = RecipeAdd(request.user)

    return render(request, html, {'form': form})


@staff_member_required()
def signup_view(request):

    html = 'signup.html'

    form = SignupForm(None or request.POST)

    if form.is_valid():
        data = form.cleaned_data
        user = User.objects.create_user(
            data['username'], data['email'], data['password']
        )
        Author.objects.create(
                name=data['name'],
                bio=data['bio'],
                user=user
            )
        login(request, user)
        return HttpResponseRedirect(reverse('index'))
    return render(request, html, {'form': form})


def login_view(request):
    html = 'login.html'

    form = LoginForm(None or request.POST)

    if form.is_valid():
        data = form.cleaned_data
        user = authenticate(
            username=data['username'], password=data['password'])
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))

    return render(request, html, {'form': form})


def logout_view(request):
        logout(request)
        return HttpResponseRedirect(reverse('index'))


class RecipeEdit(LoginRequiredMixin, UpdateView):
    model = Recipe
    fields = ['name', 'description', 'time_required', 'instructions']

    def get_success_url(self):
        return reverse('index')


def favorite_add(request, pk):
    recipe = Recipe.objects.filter(id=pk).first()
    if recipe in request.user.author.favorites.all():
        request.user.author.favorites.remove(recipe)
    else:
        request.user.author.favorites.add(recipe)
    return HttpResponseRedirect('/recipes/{}'.format(recipe.id))
