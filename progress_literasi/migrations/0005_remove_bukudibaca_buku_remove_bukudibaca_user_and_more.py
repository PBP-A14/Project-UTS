# Generated by Django 4.2.6 on 2023-10-27 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('progress_literasi', '0004_alter_targetharian_tanggal_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bukudibaca',
            name='buku',
        ),
        migrations.RemoveField(
            model_name='bukudibaca',
            name='user',
        ),
        migrations.RemoveField(
            model_name='progressbaca',
            name='buku',
        ),
        migrations.DeleteModel(
            name='BukuDibaca',
        ),
    ]
