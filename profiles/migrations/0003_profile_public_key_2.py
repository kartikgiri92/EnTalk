# Generated by Django 3.0.3 on 2020-04-13 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20200114_1836'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='public_key_2',
            field=models.CharField(default=12, max_length=30),
            preserve_default=False,
        ),
    ]
