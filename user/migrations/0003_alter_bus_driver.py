# Generated by Django 3.2.4 on 2021-06-14 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_driver_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bus',
            name='driver',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.driver'),
        ),
    ]
