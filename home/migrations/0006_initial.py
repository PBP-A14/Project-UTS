# Generated by Django 4.2.6 on 2023-10-21 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0005_delete_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('authors', models.CharField(max_length=255, verbose_name='authors')),
                ('isbn', models.CharField(max_length=150, verbose_name='isbn')),
                ('isbn13', models.CharField(max_length=150, verbose_name='isbn 13')),
                ('num_pages', models.IntegerField(verbose_name='number of pages')),
                ('publisher', models.CharField(max_length=150, verbose_name='publisher')),
            ],
        ),
    ]