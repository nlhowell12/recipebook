# Generated by Django 2.1.4 on 2018-12-12 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_author_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='favorites',
            field=models.ManyToManyField(related_name='favorites', to='recipes.Recipe'),
        ),
    ]
