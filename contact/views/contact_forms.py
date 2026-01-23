from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.db.models import Q
from django.core.paginator import Paginator
from contact.forms import ContactForm
from contact.models import Contact

def create(request):
    if request.method == 'POST':
        contactform = ContactForm(data=request.POST)

        if contactform.is_valid():
            contact = contactform.save()
            return redirect('contact:contact', contact_id=contact.pk)

        context = {
            'form': contactform
        }

        return render(request, 'contact/create.html', context)

    
    context = {
        'form': ContactForm()
    }
    return render(request, 'contact/create.html', context)
