# Generated by Django 4.1.2 on 2022-11-16 22:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysongapp', '0006_song'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='album',
            options={'verbose_name_plural': 'Artist'},
        ),
        migrations.AlterModelOptions(
            name='artist',
            options={'verbose_name_plural': 'Artist'},
        ),
        migrations.AlterModelOptions(
            name='song',
            options={'verbose_name_plural': 'Artist'},
        ),
    ]
