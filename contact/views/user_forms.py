from django.contrib import messages
from django.shortcuts import render, redirect
from contact.forms import RegisterForm, RegisterUpdateForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth


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

def login_view(request):
    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, 'Seja bem-vindo, %s!' % (user.username))
            return redirect('contact:index')

        messages.error(request, 'Usuário ou senha inválidos...')

    context = {
        'form': form,
    }

    return render(request, 'contact/login.html', context)
# 12as34df56gh

def logout_view(request):
    auth.logout(request)
    return redirect('contact:login')


def user_update(request):
    form  = RegisterUpdateForm(instance=request.user)

    if request.method != 'POST':
        return render(
            request,
            'contact/register.html',
            {'form': form}
        )
    
    form = RegisterUpdateForm(data=request.POST, instance=request.user)

    if not form.is_valid():
        return render(
            request,
            'contact/register.html',
            {'form': form}
        )
    
    form.save()

    
    context = {
        'form': form,
    }

    return render(request, 'contact/register.html', context)
