from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Feedback
import uuid


@receiver(pre_save, sender=Feedback)
def generate_feedbackID(sender, instance, **kwargs):
    if instance.id == '':
        instance.id = str(uuid.uuid4().hex)[:25]

