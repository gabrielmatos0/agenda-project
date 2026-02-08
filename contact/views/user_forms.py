from django.shortcuts import render, redirect
from contact.models import Contact
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from contact.forms import RegisterForm
from contact.models import Contact


def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()

    context = {
        'form': form,
    }

    return render(request, 'contact/register.html', context)