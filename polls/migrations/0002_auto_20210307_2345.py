# Generated by Django 3.1.7 on 2021-03-07 23:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='poem',
            options={'default_permissions': ('add', 'change', 'delete')},
        ),
    ]