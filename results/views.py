from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.views import View
# from core.models import 


@method_decorator(login_required(login_url='login'), name='get')
@method_decorator(user_passes_test(lambda user: user.is_superuser is False and user.is_staff is False), name='get')
@method_decorator(user_passes_test(lambda user: user.voter.has_voted is True), name='get')
class ElectionResultsView(View):
    template_name = 'results.html'


    def get(self, request, *args, **kwargs):

        context = {}
        return render(request, self.template_name, context)
    
