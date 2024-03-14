from .models import Feedback
from django import forms


class FeedbackForm(forms.ModelForm):
    SELECT_CHOICES = (
        (None, ''),
        ('Fair', 'Fair'),
        ('Unfair', 'Unfair'),
        ('Unsure', "I'm not sure"),
    )

    choices = forms.ChoiceField(widget=forms.CheckboxInput(attrs={
            'type': 'checkbox', 'class': 'mb-2',
        }),
    )
    description = forms.CharField(widget=forms.Textarea(attrs={
            'class': 'mb-2', 'placeholder': 'Provide additional details about your feedback/complaint',
        }),
        label='Description (optional)',
        required=False,
    )
    
    class Meta:
        model = Feedback
        fields = ('choices', 'description')