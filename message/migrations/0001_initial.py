# Generated by Django 3.2.5 on 2021-07-04 13:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(unique=True, verbose_name='Номер сообщения')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Дата сообщения')),
                ('time', models.TimeField(default=datetime.time, verbose_name='Время сообщения')),
                ('text', models.CharField(blank=True, max_length=300, null=True, verbose_name='Содержание сообщения')),
                ('file', models.FileField(blank=True, upload_to='uploads', verbose_name='Вложенный файл')),
                ('author', models.CharField(max_length=100, verbose_name='Автор сообщения')),
            ],
        ),
    ]
