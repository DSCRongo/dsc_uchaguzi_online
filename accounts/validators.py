from django.contrib.auth import get_user_model
from django.http import HttpResponse
from accounts.models import Voter


def check_registration_number_exists(request):
    """ This function validates if the typed registration number exists. """
    
    registration_num = request.POST.get('reg-no')
    reg_num_exists = Voter.objects.filter(reg_no__iexact=registration_num).exists()

    if reg_num_exists:
        return HttpResponse('<div class="text-danger">Registration no. exists!</div>')
    
    else:
        return HttpResponse()
