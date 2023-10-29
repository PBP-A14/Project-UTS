# Generated by Django 4.2.6 on 2023-10-29 05:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0010_alter_book_rating'),
        ('progress_literasi', '0008_merge_20231029_1154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='targetharian',
            name='tanggal',
        ),
        migrations.AddField(
            model_name='progressbaca',
            name='buku',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.book'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='BukuDibaca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('counted', models.IntegerField(default=0)),
                ('buku', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]