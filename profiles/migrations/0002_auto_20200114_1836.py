# Generated by Django 2.2.6 on 2020-01-14 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='private_key',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='profile',
            name='public_key',
            field=models.CharField(max_length=30),
        ),
    ]
