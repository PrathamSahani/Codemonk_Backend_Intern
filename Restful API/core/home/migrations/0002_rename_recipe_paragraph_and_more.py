# Generated by Django 5.0.3 on 2024-03-29 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Recipe',
            new_name='Paragraph',
        ),
        migrations.RenameField(
            model_name='paragraph',
            old_name='recipe_description',
            new_name='paragraph_description',
        ),
        migrations.RenameField(
            model_name='paragraph',
            old_name='recipe_name',
            new_name='paragraph_name',
        ),
    ]
