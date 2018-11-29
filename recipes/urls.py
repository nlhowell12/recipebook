from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recipes/<int:recipe_id>/', views.recipe_view, name='recipe_view'),
    path('recipes/recipeadd/', views.recipe_add),
    path('authors/<int:author_id>/', views.author_view, name='author_view'),
    path('authors/authoradd/', views.author_add)
]
