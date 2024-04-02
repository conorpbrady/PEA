from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class EventEntry(models.Model):

    owner = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length = 255, blank=True)
    title = models.CharField(max_length = 255)
    tagline = models.CharField(max_length = 255, blank=True)
    link = models.CharField(max_length = 255, blank=True)
    cost = models.CharField(max_length = 255, blank=True)

class Importer(models.Model):
    pass

class XpathImporter(Importer):

    # User
    # Subscribed boolean

    url = models.CharField(max_length = 255)
    site_name = models.CharField(max_length = 255)
    events_elements_xpath = models.CharField(max_length = 255)
    date_xpath = models.CharField(max_length = 255)
    time_xpath = models.CharField(max_length = 255, blank=True)
    location_xpath = models.CharField(max_length = 255, blank=True)
    title_xpath = models.CharField(max_length = 255)
    tagline_xpath = models.CharField(max_length = 255, blank=True)
    link_xpath = models.CharField(max_length = 255, blank=True)
    cost_xpath = models.CharField(max_length = 255, blank=True)
    date_format = models.CharField(max_length = 32, blank=True)
    time_format = models.CharField(max_length = 32, blank=True)
