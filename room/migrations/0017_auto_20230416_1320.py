# Generated by Django 3.1.4 on 2023-04-16 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0016_review_trip_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='address',
            field=models.CharField(max_length=50),
        ),
    ]