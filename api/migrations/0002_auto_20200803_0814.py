# Generated by Django 3.0.5 on 2020-08-03 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='crop',
            name='mandi',
            field=models.CharField(default='Indore', max_length=100),
        ),
        migrations.AddField(
            model_name='crop',
            name='month',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='crop',
            name='rainfall',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='crop',
            name='year',
            field=models.IntegerField(default=0),
        ),
    ]
