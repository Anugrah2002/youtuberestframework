# Generated by Django 3.1.7 on 2021-03-07 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entertainment', '0005_remove_entertainmentdb_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='SaveVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('video', models.FileField(max_length=800, upload_to='tmp')),
            ],
        ),
    ]
