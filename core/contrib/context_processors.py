from core.models import ElectionsDate
from django.utils import timezone


def elections(request):
    current_dt = timezone.datetime.now().year
    latest_election_date = ElectionsDate.objects.filter(election_date__year=current_dt).first()
    
    context = {'election_is_over': latest_election_date}
    return context

