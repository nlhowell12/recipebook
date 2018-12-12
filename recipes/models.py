from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User


class Author(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorites = models.ManyToManyField(
        'Recipe', related_name='favorites', symmetrical=False)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=2000)
    time_required = models.CharField(max_length=50)
    instructions = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('recipe_edit', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name
