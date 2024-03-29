# Generated by Django 2.0 on 2018-03-09 22:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0004_auto_20180310_0149'),
        ('team', '0006_auto_20180310_0340'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerTeam',
            fields=[
                ('name', models.CharField(blank=True, max_length=40, primary_key=True, serialize=False)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='players.Player')),
                ('team', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='team.Team')),
            ],
        ),
        migrations.RemoveField(
            model_name='teamplayer',
            name='player',
        ),
        migrations.DeleteModel(
            name='TeamPlayer',
        ),
    ]
