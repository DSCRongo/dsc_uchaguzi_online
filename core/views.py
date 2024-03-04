from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View


@method_decorator(login_required(login_url='login'), name='get')
class HomepageView(View):
    template_name = 'core/homepage.html'


    def get(self, request, *args, **kwargs):

        context = {}
        return redirect(request, self.template_name, context)
    

