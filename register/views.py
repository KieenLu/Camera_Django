from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import  messages
from django.contrib.auth import login, logout , authenticate

from .forms import CreateUserForm

 
def RegisterForm(request):
    form = CreateUserForm()

    if request. method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'You have successfully registered an account' + user)
            return redirect('/login/')

    context = {'form': form}
    return render(request,'register/register.html', context )


