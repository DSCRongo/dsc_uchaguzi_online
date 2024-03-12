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
    except ElectionsDate.DoesNotExist:
        elections_date = current_dt
    
    if current_dt.strftime('%Y-%m-%d %H:%M:%S') >= elections_date.election_date.strftime('%Y-%m-%d %H:%M:%S'):
        return True
    
    return False
