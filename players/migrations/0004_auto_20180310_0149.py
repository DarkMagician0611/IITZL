# Generated by Django 2.0 on 2018-03-09 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0003_auto_20180308_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='ssn',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='player',
            name='name',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
