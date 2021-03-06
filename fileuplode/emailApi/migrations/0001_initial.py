# Generated by Django 3.2.9 on 2021-12-01 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='emailApi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('send_to', models.EmailField(max_length=100)),
                ('content', models.CharField(max_length=100)),
                ('attechment', models.FileField(upload_to='files')),
            ],
        ),
    ]
