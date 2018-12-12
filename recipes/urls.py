from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recipes/<int:recipe_id>/', views.recipe_view, name='recipe_view'),
    path('recipes/edit/<int:pk>/', views.RecipeEdit.as_view(),
         name='recipe_edit'),
    path('recipes/favorite/<int:pk>', views.favorite_add),
    path('recipes/recipeadd/', views.recipe_add),
    path('authors/<int:author_id>/', views.author_view, name='author_view'),
    path('signup/', views.signup_view),
    path('login/', views.login_view),
    path('logout/', views.logout_view)
]
