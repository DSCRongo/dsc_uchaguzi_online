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
    

    def delete(self):
        self.profile_pic.delete()
        super(User, self).delete()


class Voter(models.Model):
    id = models.CharField(max_length=25, primary_key=True, unique=True, editable=False)
    voters_name = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    reg_no = models.CharField(max_length=20, unique=True, blank=False)
    school = models.CharField(max_length=70, blank=False)
    year = models.CharField(max_length=12, blank=False)
    semester = models.CharField(max_length=1, blank=False)
    is_registered = models.BooleanField(default=False, editable=False)
    has_voted = models.BooleanField(default=False, editable=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['voters_name']
    

    def __str__(self):
        return f'{self.voters_name}'
