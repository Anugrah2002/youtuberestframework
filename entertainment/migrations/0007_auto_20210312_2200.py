# Generated by Django 3.0.5 on 2021-03-12 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entertainment', '0006_savevideo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='savevideo',
            name='video',
        ),
        migrations.AddField(
            model_name='savevideo',
            name='videoPublicId',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='savevideo',
            name='videoUrl',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
    ]
