# Generated by Django 4.2.6 on 2023-10-27 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='target_buku',
            field=models.PositiveIntegerField(default=0),
        ),
    ]