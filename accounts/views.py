from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from .forms import UserLoginForm
from .models import User

# Create your views here.

def LogIn(request):
    form = UserLoginForm()
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user_details = auth.authenticate(username=username, password=password)
            if user_details is not None:
                auth.login(request, user_details)
                return redirect('home')
    context = {'form':form}
    return render(request, 'accounts/login.html', context)

def Home(request):
    return render(request, 'accounts/home.html')