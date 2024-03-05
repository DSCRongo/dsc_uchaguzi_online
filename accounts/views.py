from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from .forms import ProfileForm, VoterRegistrationForm


class UsersLoginView(LoginView):
    template_name = 'accounts/login.html'


@method_decorator(login_required(login_url='login'), name='get')
class VoterRegistrationView(View):
    form_class = VoterRegistrationForm
    template_name = 'accounts/register.html'

    
    def get(self, request, *args, **kwargs):
        form = VoterRegistrationForm()

        context = {'VoterRegistrationForm': form}
        return render(request, self.template_name, context)
    

    def post(self, request, *args, **kwargs):
        form = VoterRegistrationForm(request.POST)

        if form.is_valid():
            register_voter = form.save(commit=False)
            register_voter.voters_name = request.user
            register_voter.is_registered = True
            register_voter.save()

            messages.success(request, 'Voter details submitted successfully!')
            return redirect('homepage')

        context = {'VoterRegistrationForm': form}
        return render(request, self.template_name, context)


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