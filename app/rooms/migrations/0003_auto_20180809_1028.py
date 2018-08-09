# Generated by Django 2.1 on 2018-08-09 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0002_roomreservation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rooms',
            name='rooms_tag',
            field=models.CharField(blank=True, help_text='검색에 사용될 지역 태그를 입력하세요', max_length=20, verbose_name='태그'),
        ),
    ]
