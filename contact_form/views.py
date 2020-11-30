from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from contact_form.forms import ContactForm


def index(request):
    return render(request, 'index.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('contact_form:thanks'))
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def thanks(request):
    return render(request, 'thanks.html')
