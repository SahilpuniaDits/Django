# Generated by Django 3.2.9 on 2021-11-30 12:17

from django.db import migrations, models
import uplode_api.models


class Migration(migrations.Migration):

    dependencies = [
        ('uplode_api', '0004_auto_20211130_1622'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='picture',
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile', validators=[uplode_api.models.image_size]),
        ),
    ]