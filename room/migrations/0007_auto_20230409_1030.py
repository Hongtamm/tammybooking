# Generated by Django 3.1.4 on 2023-04-09 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0006_review_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomservices',
            name='servicesType',
            field=models.CharField(choices=[('Food', 'Food'), ('Drink', 'Drink'), ('Cleaning', 'Cleaning'), ('Technical', 'Technical')], max_length=20),
        ),
    ]
