# Generated by Django 4.1.5 on 2023-02-22 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_songs_author_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='songs',
            name='author',
        ),
    ]
