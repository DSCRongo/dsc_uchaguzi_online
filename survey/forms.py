from .models import Feedback
from django import forms


class FeedbackForm(forms.ModelForm):
    SELECT_CHOICES = (
        ('Fair', 'Fair'),
        ('Unfair', 'Unfair'),
        ('Unsure', "I'm not sure"),
    )

    options = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(attrs={
            'type': 'checkbox', 'class': 'mb-2',
        }),
        label='How was the election conducted?',
        choices=SELECT_CHOICES,
    )
    rating = forms.CharField(widget=forms.NumberInput(attrs={
            'type': 'number', 
            'class': 'form-control', 
            'min': 0,
            'max': 5,
        }),
        label='How do you rate the electoral process?',
        help_text='How do you rate the electoral process?'
    )
    description = forms.CharField(widget=forms.Textarea(attrs={
            'class': 'form-control', 
            'placeholder': 'Provide additional details for your feedback/complaint about GDSC Uchaguzi platform ...',
        }),
        label='Description (optional)',
        required=False,
    )

    class Meta:
        model = Feedback
        fields = ('options', 'rating', 'description')