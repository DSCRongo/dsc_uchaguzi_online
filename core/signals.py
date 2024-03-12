from .models import Aspirant, VotingRecord, ElectionsDate
from django.db.models.signals import pre_save
from django.dispatch import receiver
import uuid


@receiver(pre_save, sender=Aspirant)
def generate_aspirantID(sender, instance, **kwargs):
    if instance.id == '':
        instance.id = str(uuid.uuid4().hex)[:25]


@receiver(pre_save, sender=VotingRecord)
def generate_voter_recordID(sender, instance, **kwargs):
    if instance.id == '':
        instance.id = str(uuid.uuid4().hex)[:25]


@receiver(pre_save, sender=ElectionsDate)
def generate_voter_recordID(sender, instance, **kwargs):
    if instance.id == '':
        instance.id = str(uuid.uuid4().hex)[:25]