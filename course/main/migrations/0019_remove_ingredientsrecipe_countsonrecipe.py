# Generated by Django 2.2.10 on 2021-06-21 16:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20210621_1932'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredientsrecipe',
            name='CountsOnRecipe',
        ),
    ]
