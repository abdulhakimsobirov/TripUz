# Generated by Django 3.2.4 on 2021-06-14 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_bus_driver'),
        ('trip', '0003_alter_trip_datatime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='driver',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='user.driver'),
        ),
    ]
