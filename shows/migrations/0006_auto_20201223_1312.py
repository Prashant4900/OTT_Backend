# Generated by Django 3.1.4 on 2020-12-23 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0005_auto_20201223_1308'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='showslist',
            name='Genre',
        ),
        migrations.AddField(
            model_name='showslist',
            name='Genre',
            field=models.ManyToManyField(related_name='Genre', to='shows.Genres', verbose_name='Category'),
        ),
    ]
