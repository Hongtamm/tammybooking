# Generated by Django 3.1.4 on 2023-04-16 09:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0015_auto_20230415_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='trip_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]