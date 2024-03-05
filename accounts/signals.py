from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone
from .models import User, Voter
import uuid


@receiver(pre_save, sender=User)
def generate_userID(sender, instance, **kwargs):
    if instance.id == '':
        instance.id = str(uuid.uuid4().hex)[:25]
    
    try:
        # Calculate a user's age
        if not instance.is_superuser:
            if timezone.datetime.now().strftime('%Y-%m-%d %H:%M:%S') > instance.date_joined.strftime('%Y-%m-%d %H:%M:%S'):
                user_dob = instance.dob
                current_date = timezone.datetime.now().date()
                age = current_date - user_dob
                instance.age = int(age.days/365.25)
                
            else:
                user_dob = instance.dob
                current_date = timezone.datetime.now().date()
                age = current_date - user_dob
                instance.age = int(age.days/365.25)
    
    except (AttributeError, TypeError):    # ignore AttributeError or TypeError
        return


@receiver(pre_save, sender=Voter)
def generate_voterID(sender, instance, **kwargs):
    if instance.id == '':
        instance.id = str(uuid.uuid4().hex)[:25]

