# Generated by Django 4.0.5 on 2022-06-22 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_hotel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='management',
            name='Occupant_Occupation',
            field=models.CharField(max_length=150),
        ),
    ]
