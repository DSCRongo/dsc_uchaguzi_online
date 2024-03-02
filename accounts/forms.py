from django import forms
from .models import User


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'gender', 'mobile_no', 'dob', 'age', 'profile_pic']
