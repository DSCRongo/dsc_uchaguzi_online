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
        label='How was the election conducted?',
    )
    rating = forms.CharField(widget=forms.NumberInput(attrs={
            'type': 'number', 'class': 'mb-2',
        }),
        label='How do you rate the electoral process?',
        help_text='Range is <b>1</b> to <b>5</b>'
    )
    description = forms.CharField(widget=forms.Textarea(attrs={
            'class': 'mb-1', 
            'placeholder': 'Provide additional details about your feedback/complaint about GDSC Uchaguzi platform ...',
        }),
        label='Description (optional)',
        required=False,
    )

    class Meta:
        model = Feedback
        fields = ('choices', 'rating', 'description')