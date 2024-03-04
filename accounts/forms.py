from django import forms
from .models import User, Voter
from .utils import is_image_file



class VoterRegistrationForm(forms.ModelForm):
    SELECT_SCHOOL = (
        (None, '-- Select your school --'),
        ('School of Arts, Social Sciences and Business', 'School of Arts, Social Sciences and Business (SASSB)'),
        ('School of Education', 'School of Education (SE)'),
        ('School of Information, Communication & Media Studies', 'School of Information, Communication & Media Studies (INFOCOMS)'),
        ('School of Science, Agriculture & Environmental Science', 'School of Science, Agriculture & Environmental Science (SSAES)'),
    )
    SELECT_YEAR = (
        (None, '-- Select year of study --'),
        ('First Year', 'First Year (Fresher)'),
        ('Second Year', 'Second Year (Sophomore)'),
        ('Third Year', 'Third Year (Junior)'),
        ('Fourth Year', 'Fourth Year (Senior)'),
    )
    SELECT_SEMESTER = (
        (None, '-- Select semester --'),
        ('1', '1'),
        ('2', '2')
    )

    school = forms.ChoiceField(widget=forms.Select(attrs={
            'type': 'select', 'class': 'mb-2',
        }), 
        choices=SELECT_SCHOOL
    )
    reg_no = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'text', 'class': 'mb-2', 'placeholder': 'Enter your Registration No.',
        }),
    )
    year = forms.ChoiceField(widget=forms.Select(attrs={
            'type': 'select', 'class': 'mb-2',
        }), 
        choices=SELECT_YEAR,
    )
    semester = forms.ChoiceField(widget=forms.Select(attrs={
            'type': 'select', 'class': 'mb-2',
        }), 
        choices=SELECT_SEMESTER,
    )


    class Meta:
        model = Voter
        fields = ['reg_no', 'school', 'year', 'semester']


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
