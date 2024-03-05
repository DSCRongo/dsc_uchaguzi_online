from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone
from .models import User, Voter
import uuid


@receiver(pre_save, sender=User)
def generate_userID(sender, instance, **kwargs):
    if instance.id == '':
        instance.id = str(uuid.uuid4().hex)[:25]


@receiver(pre_save, sender=Voter)
def generate_voterID(sender, instance, **kwargs):
    if instance.id == '':
        instance.id = str(uuid.uuid4().hex)[:25]

