# Generated by Django 5.1.4 on 2024-12-21 17:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_alter_movie_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moments',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_moments', to='movie.movie'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='country',
            field=models.ManyToManyField(related_name='movies', to='movie.country'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='year',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='movielanguages',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movies_videos', to='movie.movie'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rating', to='movie.movie'),
        ),
    ]
