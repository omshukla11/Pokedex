# Generated by Django 3.2.3 on 2021-07-29 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0002_rename_height_pokeclass_weight'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Pokeclass',
            new_name='Poke_class',
        ),
    ]