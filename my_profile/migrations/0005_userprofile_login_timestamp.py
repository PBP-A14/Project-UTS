# Generated by Django 4.2.6 on 2023-10-27 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_profile', '0004_remove_userprofile_active_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='login_timestamp',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
