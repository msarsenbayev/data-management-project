# Generated by Django 3.2.6 on 2023-05-04 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_management_app', '0002_alter_valvedetails_valve_serial_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='valvedetails',
            name='valve_serial_number',
            field=models.CharField(max_length=25, unique=True),
        ),
    ]