# Generated by Django 3.2.3 on 2021-07-30 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0008_auto_20210730_1825'),
    ]

    operations = [
        migrations.RenameField(
            model_name='poke_class',
            old_name='image_url',
            new_name='back_url',
        ),
        migrations.RemoveField(
            model_name='poke_class',
            name='image_file',
        ),
        migrations.AddField(
            model_name='poke_class',
            name='front_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]