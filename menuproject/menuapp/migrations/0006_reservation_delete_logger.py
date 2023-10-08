# Generated by Django 4.2.5 on 2023-10-06 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menuapp', '0005_logger_remove_vehicle_customer_delete_customer_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('contact', models.CharField(max_length=300, verbose_name='Phone number')),
                ('time', models.TimeField()),
                ('count', models.IntegerField()),
                ('notes', models.CharField(blank=True, max_length=300)),
            ],
        ),
        migrations.DeleteModel(
            name='Logger',
        ),
    ]
