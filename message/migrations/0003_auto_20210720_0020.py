# Generated by Django 3.2.5 on 2021-07-19 21:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0002_alter_email_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='created_at',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='email',
            name='file',
            field=models.FileField(blank=True, upload_to='uploads/', verbose_name='Вложенный файл'),
        ),
    ]