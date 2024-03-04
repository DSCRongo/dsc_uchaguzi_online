from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser
from django.db import models
from PIL import Image


def user_path_directory(instance, filename):
    """ media path is in the format MEDIA_ROOT/user_{username}/profile-pics/{filename}. """
    return 'user_{}/profile-pics/{}'.format(instance.username, filename)


class User(AbstractUser):
    id = models.CharField(max_length=25, primary_key=True, unique=True, editable=False)
    email = models.EmailField(unique=True, blank=False)
    gender = models.CharField(max_length=7, blank=False)
    mobile_no = PhoneNumberField(blank=False)
    dob = models.DateField(null=True, blank=False)
    age = models.PositiveIntegerField(default=0)
    profile_pic = models.ImageField(upload_to=user_path_directory, default='default.png')
    date_updated = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    
    class Meta:
        ordering = ['first_name', 'last_name', 'username']


    def __str__(self):
        return self.username


    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)

        dp = Image.open(self.profile_pic.path)

        if dp.height > 400 and dp.width > 400:
            output_size = (480, 480)
            dp.thumbnail(output_size)
            dp.save(self.profile_pic.path)
    
