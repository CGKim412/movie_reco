# Generated by Django 3.0.4 on 2020-03-14 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_auto_20200219_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.TextField(null=True, verbose_name='poster URL'),
        ),
    ]
