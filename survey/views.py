from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from .forms import FeedbackForm


@method_decorator(login_required(login_url='login'), name='get')
@method_decorator(user_passes_test(lambda user: user.is_superuser is False and user.is_staff is False), name='get')
@method_decorator(user_passes_test(lambda user: user.voter.has_voted is True), name='get')
class SubmitFeedbackView(View):
    form_class = FeedbackForm
    template_name = 'survey/feedback.html'


    def get(self, request, *args, **kwargs):
        feedback_form = self.form_class()

        context = {'FeedbackForm': feedback_form}
        return render(request, self.template_name, context)
    

    def post(self, request, *args, **kwargs):
        feedback_form = self.form_class(request.POST)

        if feedback_form.is_valid():
            feedback_form.save()
            messages.info(request, 'Form submitted successfully! Thank you for your feedback.')
            return redirect('feedback')

        context = {'FeedbackForm': feedback_form}
        return render(request, self.template_name, context)