# Generated by Django 2.0 on 2018-03-09 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('players', '0003_auto_20180308_1658'),
    ]

    operations = [
        migrations.CreateModel(
            name='BallRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balls', models.IntegerField(default=0)),
                ('runs', models.IntegerField(default=0)),
                ('wickets', models.IntegerField(default=0)),
                ('points', models.IntegerField(default=0)),
                ('player', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='players.Player')),
            ],
        ),
        migrations.CreateModel(
            name='BatRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('runs', models.IntegerField(default=0)),
                ('balls', models.IntegerField(default=0)),
                ('fours', models.IntegerField(default=0)),
                ('sixes', models.IntegerField(default=0)),
                ('points', models.IntegerField(default=0)),
                ('player', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='players.Player')),
            ],
        ),
        migrations.CreateModel(
            name='FieldRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catches', models.IntegerField(default=0)),
                ('stumps', models.IntegerField(default=0)),
                ('run_outs', models.IntegerField(default=0)),
                ('points', models.IntegerField(default=0)),
                ('player', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='players.Player')),
            ],
        ),
    ]
