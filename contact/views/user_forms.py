from django.contrib import messages
from django.shortcuts import render
from contact.forms import RegisterForm


def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, f'Usuário cadastrado com sucesso!')

    context = {
        'form': form,
    }

    return render(request, 'contact/register.html', context)