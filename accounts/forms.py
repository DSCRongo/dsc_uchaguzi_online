from django import forms
from .models import User
from .utils import is_image_file


class ProfileForm(forms.ModelForm):
    profile_pic = forms.FileField(
        widget=forms.FileInput(attrs={
            'type': 'file', 'class': 'form-control mb-2', 'accept': '.jpg, .jpeg, .png',
        }),
        required=False,
        validators=[is_image_file],
    )

    class Meta:
        model = User
        fields = ['email', 'gender', 'mobile_no', 'dob', 'age', 'profile_pic']
