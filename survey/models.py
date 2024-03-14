from django.db import models


class Feedback(models.Model):
    id = models.CharField(max_length=25, primary_key=True, unique=True, editable=False)
    choices = models.CharField(max_length=10, blank=False)
    rating = models.PositiveIntegerField(default=0)
    description = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['-date_created']
        verbose_name_plural = 'Feedback'


    def __str__(self):
        return self.id
    
