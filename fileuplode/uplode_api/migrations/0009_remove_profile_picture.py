# Generated by Django 3.2.9 on 2021-12-02 05:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uplode_api', '0008_remove_profile_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='picture',
        ),
    ]
