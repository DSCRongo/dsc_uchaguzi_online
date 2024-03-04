from accounts.models import User
from django.db import models
from PIL import Image


def user_path_directory(instance, filename):
    """ media path is in the format MEDIA_ROOT/user_{username}/profile-pics/{filename}. """
    return 'aspirant_{}/dps/{}'.format(str(instance.post.username)[:5], filename)


class Voter(models.Model):
    id = models.CharField(max_length=25, primary_key=True, unique=True, editable=False)
    voters_name = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    reg_no = models.CharField(max_length=20, blank=False)
    school = models.CharField(max_length=10, blank=False)
    year = models.CharField(max_length=12, blank=False)
    semester = models.CharField(max_length=1, blank=False)
    is_registered = models.BooleanField(default=False, editable=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['voters_name']
    

    def __str__(self):
        return f'{self.voters_name}'


class Aspirant(models.Model):
    id = models.CharField(max_length=25, primary_key=True, unique=True, editable=False)
    name = models.OneToOneField(Voter, on_delete=models.CASCADE, editable=False)
    post = models.CharField(max_length=30, blank=False)
    total_votes = models.PositiveIntegerField(default=0, editable=False)
    aspirant_dp = models.ImageField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    
    class Meta:
        ordering = ['name', 'post']
    

    def __str__(self):
        return f'{self.name}'
    

    def save(self, *args, **kwargs):
        super(Aspirant, self).save(*args, **kwargs)

        dp = Image.open(self.aspirant_dp.path)
        if dp.height > 400 and dp.width > 400:
            output_size = (480, 480)
            dp.thumbnail(output_size)
            dp.save(self.aspirant_dp.path)
    

class VotingRecord(models.Model):
    id = models.CharField(max_length=25, primary_key=True, unique=True, editable=False)
    elected_post = models.ForeignKey(Aspirant, on_delete=models.CASCADE, editable=False)
    voter = models.ForeignKey(Voter, on_delete=models.CASCADE, editable=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['elected_post', 'voter']
    

    def __str__(self):
        return f'{self.elected_post}'
    
