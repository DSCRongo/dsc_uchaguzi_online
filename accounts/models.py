from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser
from django.db import models


def user_path_directory(instance, filename):
    """ media path is in the format MEDIA_ROOT/user_{username}/profile-pics/{filename}. """
    return 'user_{}/profile-pics/{}'.format(instance.username, filename)


class User(AbstractUser):
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=7, blank=False)
    mobile_no = PhoneNumberField(blank=False)
    dob = models.DateField(null=True)
    age = models.PositiveIntegerField(default=0)
    profile_pic = models.ImageField(upload_to=user_path_directory, default='default.jpg')
    date_updated = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
