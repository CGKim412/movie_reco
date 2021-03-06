# Generated by Django 3.0.4 on 2020-03-15 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_auto_20200314_1407'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='tmdb_ok',
        ),
        migrations.AddField(
            model_name='movie',
            name='use_alt_poster',
            field=models.BooleanField(default=True, verbose_name='Use alternate poster?'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='is_init_state',
            field=models.BooleanField(default=True, verbose_name='Is initial state?'),
        ),
    ]
