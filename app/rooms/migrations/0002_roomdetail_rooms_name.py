# Generated by Django 2.0.7 on 2018-08-01 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='roomdetail',
            name='rooms_name',
            field=models.CharField(default='<django.db.models.query_utils.DeferredAttribute object at 0x1096de400>', max_length=50),
        ),
    ]
