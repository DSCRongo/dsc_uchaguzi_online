from accounts.models import User, Voter
from django.db import models
from PIL import Image


def user_path_directory(instance, filename):
    """ media path is in the format MEDIA_ROOT/user_{username}/profile-pics/{filename}. """
    return 'aspirant_{}/dps/{}'.format(str(instance.name), filename)


class Aspirant(models.Model):
    id = models.CharField(max_length=25, primary_key=True, unique=True, editable=False)
    name = models.OneToOneField(Voter, on_delete=models.CASCADE)
    post = models.CharField(max_length=30, blank=False)
    total_votes = models.PositiveIntegerField(default=0, editable=False)
    aspirant_dp = models.ImageField(upload_to=user_path_directory, null=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    
    class Meta:
        ordering = ['name', 'post']
    

    def __str__(self):
        return f'{self.name}'
    

    def save(self, *args, **kwargs):
        super(Aspirant, self).save(*args, **kwargs)
        dp = Image.open(self.aspirant_dp.path)

        if dp.height > 120 and dp.width > 120:
            output_size = (320, 320)
            dp.thumbnail(output_size)
            dp.save(self.aspirant_dp.path)
    

    def delete(self):
        self.aspirant_dp.delete()
        super(Aspirant, self).delete()
    

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
    

class ElectionsDate(models.Model):
    id = models.CharField(max_length=25, primary_key=True, unique=True, editable=False)
    election_date = models.DateTimeField(null=False, blank=False)
    is_done = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-date_created']
        verbose_name_plural = 'Elections date'
    

    def __str__(self):
        return f'{self.election_date}'
    

