# Generated by Django 2.0 on 2018-03-09 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0003_remove_team_substitutions'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
