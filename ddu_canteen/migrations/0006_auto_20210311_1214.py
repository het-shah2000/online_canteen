# Generated by Django 3.1.5 on 2021-03-11 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ddu_canteen', '0005_auto_20210311_1145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='email',
        ),
        migrations.RemoveField(
            model_name='student',
            name='name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='password',
        ),
    ]
