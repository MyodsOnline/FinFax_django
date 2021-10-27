from django.db import models
import datetime
from django.utils.timezone import now


# Create your models here.
class Email(models.Model):
    number = models.PositiveIntegerField(verbose_name='Номер сообщения', unique=True)
    date = models.DateField(verbose_name='Дата сообщения', default=datetime.date.today)
    time = models.TimeField(verbose_name='Время сообщения')
    text = models.CharField('Содержание сообщения', max_length=300, blank=True, null=True)
    file = models.FileField(verbose_name='Вложенный файл', upload_to='uploads/', blank=True)
    author = models.CharField(verbose_name='Автор сообщения', max_length=100)
    created_at = models.DateTimeField(default=now, blank=True)

    def __str__(self):
        return f'{self.number} | {self.date} | {self.time} | {self.author} | {self.file}'
