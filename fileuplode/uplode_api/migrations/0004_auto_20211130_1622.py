# Generated by Django 3.2.9 on 2021-11-30 10:52

from django.db import migrations, models
import uplode_api.models


class Migration(migrations.Migration):

    dependencies = [
        ('uplode_api', '0003_remove_profile_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='picture',
        ),
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile', validators=[uplode_api.models.profile.save]),
        ),
    ]
