# Generated by Django 3.2.9 on 2021-12-15 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registerotp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='verification_otp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otp', models.IntegerField()),
            ],
        ),
    ]