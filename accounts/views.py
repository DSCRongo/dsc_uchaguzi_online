from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.contrib import messages
from django.template import loader
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

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        
        # Prevent caching of the page
        response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
        response['Expires'] = '0'
        
        # Add JavaScript redirect to display "Document Expired" on back button press
        template = loader.get_template('document-expired.html')
        document_expired_script = template.render()
        response.content = document_expired_script

        return response
    
def document_expired_view(request):
    return render(request, 'document-expired.html')
