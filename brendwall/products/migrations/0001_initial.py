# Generated by Django 4.2.16 on 2024-09-13 14:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Название')),
                ('description', models.TextField(max_length=256, verbose_name='Описание')),
                ('price', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Цена')),
            ],
        ),
    ]
