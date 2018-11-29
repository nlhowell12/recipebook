from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField()

class Recipe(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=2000)
    time_required = models.CharField(max_length=50)
    instructions = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)