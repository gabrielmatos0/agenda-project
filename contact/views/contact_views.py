from django.shortcuts import render
from contact.models import Contact

def index(request):
    contacts = Contact.objects.filter(show=True, phone__startswith="+55")

    context = {
        'contacts': contacts
    }

    return render(request, 'contact/index.html', context)
