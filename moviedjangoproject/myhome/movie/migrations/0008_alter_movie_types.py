# Generated by Django 5.1.4 on 2024-12-28 18:07

import multiselectfield.db.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0007_rating_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='types',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('144', '144'), ('360', '360'), ('480', '480'), ('720', '720'), ('1080', '1080')], max_length=160),
        ),
    ]
