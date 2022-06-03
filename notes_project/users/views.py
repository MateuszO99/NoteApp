from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import UserRegisterForm


def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            login_user = authenticate(username=username, password=password)
            login(request, login_user)
            messages.success(request, f'Account created for {username}')
            return redirect('notes')
    else:
        form = UserRegisterForm()
    return render(request, 'users/user_register.html', {'form': form})
