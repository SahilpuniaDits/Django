# Generated by Django 3.2.9 on 2021-12-01 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emailApi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailapi',
            name='attechment',
            field=models.FileField(upload_to='media'),
        ),
    ]