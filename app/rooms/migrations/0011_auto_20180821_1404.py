# Generated by Django 2.1 on 2018-08-21 05:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0010_auto_20180821_1235'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservationreserved',
            old_name='reservations',
            new_name='disable_days',
        ),
    ]