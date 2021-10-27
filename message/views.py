from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.utils.timezone import timezone
from django.urls import reverse
from django import forms

from .models import Email
from .forms import EmailForm


# Create your views here.
def index(request):
    error = ''
    if request.method == 'POST':
        form = EmailForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = EmailForm()

    emails = Email.objects.all()
    content = {
        'emails': emails,
        'form': form,
        'error': error,
    }
    return render(request, 'message/index.html', content)


def orders(request):
    content = {'header': 'Fingrid Orders'}
    return render(request, 'message/orders.html', content)
