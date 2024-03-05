from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from django.views import View
from .models import Aspirant, VotingRecord
from accounts.models import Voter


@method_decorator(login_required(login_url='login'), name='get')
class HomepageView(View):
    template_name = 'core/homepage.html'


    def get(self, request, *args, **kwargs):

        context = {}
        return render(request, self.template_name, context)
    

@method_decorator(login_required(login_url='login'), name='get')
class VotingView(View):
    template_name = 'core/vote.html'


    def get(self, request, voter_id, *args, **kwargs):
        current_year = timezone.datetime.now().year
        aspirant_qs = Aspirant.objects.filter(date_created__year=current_year)

        context = {'aspirants': aspirant_qs}
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
            voter_info

            # update voter's record
            get_voter = Voter.objects.get(voters_name=request.user)
            get_voter.has_voted = True
            get_voter.save()

            messages.success(request, 'Your vote was successfully submitted!')
            return redirect('cast_vote', voter_id)

        context = {}
        return render(request, self.template_name, context)
