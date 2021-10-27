from django.forms import ModelForm
from django import forms
from .models import Email


class EmailForm(ModelForm):
    class Meta:
        model = Email
        fields = ['number', 'date', 'time', 'text', 'file', 'author']
        widgets = {
            'number': forms.NumberInput(attrs={'class': 'inputs'}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'inputs'}),
            'time': forms.TimeInput(attrs={'type': 'time', 'class': 'inputs'}),
            'text': forms.Textarea(attrs={'rows': 8, 'placeholder': 'Text', 'class': 'inputs_xl'}),
            'file': forms.FileInput(attrs={'class': 'inputs_xl'}),
            'author': forms.TextInput(attrs={'class': 'inputs_xl'})
        }

        number = forms.DecimalField(label='Номер:',)
        date = forms.DateField(label='Дата:',)
        time = forms.TimeField(label='Время:',)
        text = forms.CharField(label='Текст:', required=False)
        file = forms.FileField(label='Файл:', required=False)
        author = forms.CharField(label='Автор:',)
