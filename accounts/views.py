from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from .forms import ProfileForm, VoterRegistrationForm


class UsersLoginView(LoginView):
    template_name = 'accounts/login.html'


@login_required(login_url='login')
def profileView(request):
    profile_form = ProfileForm(instance=request.user)
    password_change_form = PasswordChangeForm(request.user)

    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user)
        password_change_form = PasswordChangeForm(request.user, data=request.POST)

        if profile_form.is_valid():
            profile_form.save()
            messages.info(request, 'Account updated')
            return redirect('user_profile')
        
        if password_change_form.is_valid():
            user = password_change_form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('user_profile')

    context = {'form':profile_form, 'ChangePasswordForm': password_change_form}
    return render(request, 'accounts/profile.html', context)


class LogoutUsersView(LogoutView):
    template_name = 'accounts/login.html'