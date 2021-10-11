from django.shortcuts import render
from django.contrib.auth import login, authenticate 

from . import forms

# Create your views here.
def login_page(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['passeword'],
            )
            if user is not None:
                login(request, user)
                message = f'Bonjour, {user.username}! Vous êtes connecté.'
            else:
                message = 'Identifiant invalide.'
    return render(request, 'authentification/login.html', context={'form': form, 'message': message})