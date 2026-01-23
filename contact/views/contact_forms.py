from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.db.models import Q
from django.core.paginator import Paginator
from contact.forms import ContactForm


def create(request):
    if request.method == 'POST':
        contactform = ContactForm(data=request.POST)

        context = {
            'form': contactform
        }

        return render(request, 'contact/create.html', context)

    
    context = {
        'form': ContactForm()
    }
    return render(request, 'contact/create.html', context)
