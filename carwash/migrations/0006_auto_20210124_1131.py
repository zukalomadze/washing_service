# Generated by Django 3.1.5 on 2021-01-24 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carwash', '0005_booth_car'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='salary',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
    ]
