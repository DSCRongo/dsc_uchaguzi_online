from django import forms
from .models import User
from .utils import is_image_file


class ProfileForm(forms.ModelForm):
    SELECT_GENDER = (
        (None, '-- Select gender --'),
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    email = forms.EmailField(widget=forms.EmailInput(), disabled=True)
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), disabled=True)
    gender = forms.ChoiceField(widget=forms.Select(attrs={
            'type': 'select',
        }),
        choices=SELECT_GENDER,
        disabled=True,
    )
    profile_pic = forms.FileField(
        widget=forms.FileInput(attrs={
            'type': 'file', 'class': 'form-control mb-2', 'accept': '.jpg, .jpeg, .png',
        }),
        required=False,
        validators=[is_image_file],
    )

    class Meta:
        model = User
        fields = ['email', 'gender', 'dob', 'mobile_no', 'profile_pic']
