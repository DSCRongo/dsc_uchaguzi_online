from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required


class UsersLoginView(LoginView):
    template_name = 'accounts/login.html'


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


class LogoutUsersView(LogoutView):
    template_name = 'accounts/login.html'