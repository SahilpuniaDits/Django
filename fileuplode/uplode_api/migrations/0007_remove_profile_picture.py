# Generated by Django 3.2.9 on 2021-12-01 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uplode_api', '0006_auto_20211201_1711'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='picture',
        ),
    ]
