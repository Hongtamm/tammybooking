# Generated by Django 3.1.4 on 2023-02-20 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='comment',
            field=models.TextField(default=''),
        ),
    ]
