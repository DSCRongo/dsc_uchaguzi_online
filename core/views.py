from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from django.views import View
from .models import Aspirant, VotingRecord, ElectionsDate
from accounts.models import Voter
from accounts.forms import VoterRegistrationForm


@method_decorator(login_required(login_url='login'), name='get')
@method_decorator(user_passes_test(lambda user: user.is_superuser is False and user.is_staff is False), name='get')
class HomepageView(View):
    form_class = VoterRegistrationForm
    template_name = 'core/homepage.html'


    def get(self, request, *args, **kwargs):
        form = self.form_class()
        current_year = timezone.datetime.now().year
        total_voters = Voter.objects.count()
        aspirants = Aspirant.objects.filter(date_created__year=current_year)
        male_registered_voters = Voter.objects.filter(voters_name__gender='Male').count()   # Males
        female_registered_voters = Voter.objects.filter(voters_name__gender='Female').count()    # Females
        get_elections_date = ElectionsDate.objects.filter(date_created__year=current_year).first()

        context = {
            'VoterRegistrationForm': form,
            'TotalVoters': total_voters,
            'aspirants': aspirants,
            'MaleRegisteredVoters': male_registered_voters,
            'FemaleRegisteredVoters': female_registered_voters,
            'elections_date': get_elections_date,
        }
        return render(request, self.template_name, context)
    

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            register_voter = form.save(commit=False)
            register_voter.voters_name = request.user
            register_voter.is_registered = True
            register_voter.save()

            messages.success(request, 'Voter details submitted successfully!')
            return redirect('homepage')

        context = {'VoterRegistrationForm': form}
        return render(request, self.template_name, context)
    

@method_decorator(login_required(login_url='login'), name='get')
@method_decorator(user_passes_test(lambda user: user.is_superuser is False and user.is_staff is False), name='get')
class VotingView(View):
    template_name = 'core/vote.html'


    def get(self, request, voter_id, *args, **kwargs):
        current_year = timezone.datetime.now().year
        aspirant_qs = Aspirant.objects.filter(date_created__year=current_year)
        get_elections_date = ElectionsDate.objects.filter(date_created__year=current_year).first()

        context = {'aspirants': aspirant_qs, 'elections_date': get_elections_date}
        return render(request, self.template_name, context)
    

    def post(self, request, voter_id, *args, **kwargs):
        _aspirant = request.POST.get('elected-lead')

        if _aspirant:
            # update elected aspirant record in db
            voter_obj = Voter.objects.get(voters_name__username=_aspirant).id
            get_aspirant = Aspirant.objects.get(name_id=voter_obj)
            get_aspirant.total_votes += 1
            get_aspirant.save()

            # save voters details in db
            voter_info, created = VotingRecord.objects.get_or_create(elected_post=get_aspirant, voter=request.user.voter)
            
            # update voter's record
            get_voter = Voter.objects.get(voters_name=request.user)
            get_voter.has_voted = True
            get_voter.save()

            messages.success(request, 'Your vote was successfully submitted!')
            return redirect('cast_vote', voter_id)

        context = {}
        return render(request, self.template_name, context)
