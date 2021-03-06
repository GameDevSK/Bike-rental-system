# Generated by Django 3.1.5 on 2021-02-03 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bike',
            fields=[
                ('bike_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('bike_company', models.CharField(default=None, max_length=20)),
                ('bike_model', models.CharField(default=None, max_length=30)),
                ('reg_number', models.CharField(default='', max_length=10)),
                ('seat_capacity', models.DecimalField(decimal_places=0, default=2, max_digits=1)),
                ('rent_per_day', models.PositiveIntegerField(default=0)),
                ('driven_kms', models.PositiveIntegerField(default=0)),
                ('image', models.ImageField(default=None, upload_to='bike_pics')),
            ],
        ),
    ]
