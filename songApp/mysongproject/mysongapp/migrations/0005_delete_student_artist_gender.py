# Generated by Django 4.1.2 on 2022-10-29 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysongapp', '0004_student_remove_artist_gender'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.AddField(
            model_name='artist',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=128, null=True),
        ),
    ]
