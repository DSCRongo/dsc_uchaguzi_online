from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import User

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'gender', 'mobile_no', 'dob', 'age', 'profile_pic']