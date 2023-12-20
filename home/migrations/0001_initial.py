# Generated by Django 5.0 on 2023-12-19 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('description', models.TextField(verbose_name='description')),
                ('authors', models.CharField(max_length=255, verbose_name='authors')),
                ('isbn', models.CharField(max_length=150, verbose_name='isbn')),
                ('num_pages', models.IntegerField(verbose_name='number of pages')),
                ('publisher', models.CharField(max_length=150, verbose_name='publisher')),
                ('rating_count', models.IntegerField(verbose_name='rating count')),
                ('rating', models.FloatField(verbose_name='rating')),
            ],
        ),
    ]
