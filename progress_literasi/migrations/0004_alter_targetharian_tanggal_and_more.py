# Generated by Django 4.2.6 on 2023-10-27 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('progress_literasi', '0003_alter_aktivitasuser_waktu_aktif_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='targetharian',
            name='tanggal',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='targetharian',
            name='target_buku',
            field=models.PositiveIntegerField(),
        ),
    ]