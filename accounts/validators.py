from django.contrib.auth import get_user_model
from django.http import HttpResponse
from accounts.models import Voter


def check_registration_number_exists(request):
    """ This function validates if the typed registration number exists. """
    
    registration_num = request.POST.get('reg_no')
    print(f'Registration number: {registration_num}')
    reg_num_exists = Voter.objects.filter(reg_no__iexact=registration_num).exists()

    if reg_num_exists:
        return HttpResponse('<div class="text-danger fw-bold">Registration number provided exists!</div>')
    
    else:
        return HttpResponse()
