# Generated by Django 3.1.5 on 2021-01-23 20:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=255, verbose_name='Car Brand')),
                ('license_plate', models.CharField(max_length=255, verbose_name='License Plate')),
                ('car_type', models.PositiveSmallIntegerField(choices=[(1, 'Suv'), (2, 'Sedane'), (3, 'Hatchback'), (4, 'Other')], default=4)),
            ],
        ),
        migrations.CreateModel(
            name='CarWash',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Company Name')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=255)),
                ('street_address', models.CharField(max_length=255)),
                ('zip', models.CharField(max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('salary', models.IntegerField(verbose_name='Salary')),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carwash.carwash')),
            ],
        ),
        migrations.AddField(
            model_name='carwash',
            name='location',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='carwash.location'),
        ),
        migrations.CreateModel(
            name='Booth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booth_number', models.CharField(max_length=255, verbose_name='Booth Number')),
                ('occupied', models.BooleanField(default=False, verbose_name='Occupied')),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booth', to='carwash.carwash')),
                ('washer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='booth', to='carwash.employee')),
            ],
            options={
                'verbose_name': 'Booth',
                'verbose_name_plural': 'Booths',
            },
        ),
    ]
