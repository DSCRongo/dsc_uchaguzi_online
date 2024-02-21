from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib import messages
from .forms import UserLoginForm, ProfileForm
from django.contrib.auth.decorators import login_required
from .models import User


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


@login_required(login_url='login')
def Home(request):
    return render(request, 'accounts/home.html')


@login_required(login_url='login')
def profileView(request):
    profile_form = ProfileForm(instance=request.user)

    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user)

        if profile_form.is_valid():
            profile_form.save()
            messages.info(request, 'Account updated')
            return redirect('user_profile')

    context = {'form':profile_form}
    return render(request, 'accounts/profile.html', context)

@login_required(login_url='login')
def Logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.info(request, 'Logged Out')
        return redirect('login')
    return render(request, 'accounts/logout.html')