from core.models import ElectionsDate
from django.utils import timezone
from django import template


register = template.Library()


@register.filter(name='current_datetime')
def current_date_time(value):
    """ 
        This filter checks if the current datetime is greater than the elections date. If True, 
        it displays aspirants in the "Aspirants" table.
    """
    
    current_dt = timezone.datetime.now()

    try:
        elections_date = ElectionsDate.objects.filter(election_date=value).first()
        elections_date = elections_date.election_date
    except ElectionsDate.DoesNotExist:
        elections_date = current_dt
    
    # since time_zone is UTC, the current time is 3 hours behind the server's time.
    # To curb this the if block solve the issue
    # In the if block check if the hour and minute in the current datetime (current_dt) is
    # greater than the hour and minute in elections_date
    # if the condition is True return True else False
    if (current_dt.date() and (current_dt.hour + 3 and current_dt.minute)) >= (elections_date.date() and (elections_date.hour and elections_date.minute)):
        return True
    
    return False
