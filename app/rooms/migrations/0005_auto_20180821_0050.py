# Generated by Django 2.1 on 2018-08-20 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0004_auto_20180821_0046'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservationreserved',
            old_name='reserved',
            new_name='reservations',
        ),
        migrations.AlterField(
            model_name='reservationreserved',
            name='reservation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms.RoomReservation'),
        ),
    ]