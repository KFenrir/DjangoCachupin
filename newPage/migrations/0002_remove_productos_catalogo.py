# Generated by Django 4.1.5 on 2023-07-06 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newPage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productos',
            name='catalogo',
        ),
    ]