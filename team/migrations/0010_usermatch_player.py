# Generated by Django 2.0.3 on 2018-03-16 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0009_usermatch'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermatch',
            name='player',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
