# Generated by Django 4.2.6 on 2023-10-28 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('progress_literasi', '0006_bukudibaca_counted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='targetharian',
            name='tanggal',
        ),
        migrations.AlterField(
            model_name='targetharian',
            name='target_buku',
            field=models.PositiveIntegerField(),
        ),
        migrations.DeleteModel(
            name='AktivitasUser',
        ),
    ]