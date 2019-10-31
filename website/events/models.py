from django.db import models
# from django.contrib.auth.models import User

# Create your models here.

class Event(models.Model):
    event_name = models.CharField(max_length=128, blank=False)
    event_poster = models.ImageField(upload_to='event_posters/',blank=False,null=True)
    event_description = models.CharField(max_length=256, blank=False)
    event_date = models.DateField()
    img1 = models.ImageField(upload_to='event_img/', blank=True)
    img2 = models.ImageField(upload_to='event_img/', blank=True)
    img3 = models.ImageField(upload_to='event_img/', blank=True)
    img4 = models.ImageField(upload_to='event_img/', blank=True)
    img5 = models.ImageField(upload_to='event_img/', blank=True)
    time_choice = [
        ('f','Future'),
        ('n','Present'),
        ('p','Past'),
    ]
    event_time = models.CharField(max_length=1, choices=time_choice, default='f')
    event_winners = models.CharField(max_length=256, blank=True)
