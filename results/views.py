from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.views import View
from accounts.models import Voter
from core.models import Aspirant, VotingRecord
from survey.models import Feedback


@method_decorator(login_required(login_url='login'), name='get')
@method_decorator(user_passes_test(lambda user: user.is_superuser is False and user.is_staff is False), name='get')
@method_decorator(user_passes_test(lambda user: user.voter.has_voted is True), name='get')
class ElectionResultsView(View):
    template_name = 'results.html'


    def get(self, request, user_id, *args, **kwargs):
        # voters info.
        male_voters = Voter.objects.filter(voters_name__gender='Male', is_registered=True).count()    # total male registered voters
        female_voters = Voter.objects.filter(voters_name__gender='Female', is_registered=True).count()    # total female registered voters
        registered_voters = Voter.objects.filter(is_registered=True).count()    # total registered voters
        casted_votes = VotingRecord.objects.all().count()   # casted votes - registered voters who turned out for voting
        # feedback QS
        positive_feedback = Feedback.objects.filter(options__exact="['Fair']").count()
        negative_feedback = Feedback.objects.filter(options__exact="['Unfair']").count()
        neutral_feedback = Feedback.objects.filter(options__exact="['Unsure']").count()
        print(registered_voters, casted_votes)

        # total votes garnered
        elected_aspirants = Aspirant.objects.filter(post__icontains='gdsc lead').values('name__voters_name__username', 'total_votes')

        context = {
            'MaleRegisteredVoters': male_voters,
            'FemaleRegisteredVoters': female_voters,
            'TotalRegisteredVoters': registered_voters,
            'CastedVotes': casted_votes,
            'PositiveFeedback': positive_feedback,
            'NegativeFeedback': negative_feedback,
            'NeutralFeedback': neutral_feedback,
            'ElectedAspirants': elected_aspirants,
        }
        return render(request, self.template_name, context)
    
