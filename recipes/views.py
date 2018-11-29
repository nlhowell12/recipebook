from django.http import HttpResponse
from django.shortcuts import render

from .models import Author, Recipe
from .forms import RecipeAdd, AuthAdd


def index(request):
    recipe_list = Recipe.objects.all()
    context = {'recipe_list': recipe_list}

    return render(request, 'recipes/index.html', context)

def recipe_view(request, recipe_id):
    recipe_item = Recipe.objects.get(pk=recipe_id).instructions
    author = Recipe.objects.get(pk=recipe_id).author
    context = {
        'recipe_item': recipe_item,
        'author': author
    }
    return render(request, 'recipes/recipe_view.html', context)

def author_view(request, author_id):
    author_name = Author.objects.get(pk=author_id).name
    authors_recipes_object = Recipe.objects.filter(author__name=author_name)
    authors_recipes = []
    for recipe in authors_recipes_object:
        authors_recipes.append(recipe)
    context = {
        'author_name': author_name,
        'authors_recipes': authors_recipes
    }
    return render(request, 'authors/author_view.html', context)

def recipe_add(request):
    html = 'recipes/recipe_add.html'
    form = None

    if request.method == 'POST':
        form = RecipeAdd(request.POST)
        if form.is_valid():
            data = form.cleaned_data
        
            Recipe.objects.create(
                name=data['name'],
                description=data['description'],
                time_required=data['time_required'],
                instructions=data['instructions'],
                author=Author.objects.filter(id=data['author']).first()
            )

        return render(request, 'recipes/thanks.html')

    else:
        form = RecipeAdd()

    return render(request, html, {'form': form})

def author_add(request):
    html = 'authors/author_add.html'
    form = None

    if request.method == 'POST':
        form = AuthAdd(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            Author.objects.create(
                name=data['name'],
                bio=data['bio']
            )

        return render(request, 'recipes/thanks.html')

    else:
        form = AuthAdd()

    return render(request, html, {'form': form})