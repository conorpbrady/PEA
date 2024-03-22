from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class EventEntry(models.Model):

    owner = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length = 255)
    title = models.CharField(max_length = 255)
    tagline = models.CharField(max_length = 255)
    link = models.CharField(max_length = 255)
    cost = models.DecimalField(max_digits = 9, default = 0.00, decimal_places = 2)


class Importer(models.Model):
    pass

class XpathImporter(Importer):

    url = models.CharField(max_length = 255)
    site_name = models.CharField(max_length = 255)
    events_elements_xpath = models.CharField(max_length = 255)
    date_xpath = models.CharField(max_length = 255)
    time_xpath = models.CharField(max_length = 255)
    location_xpath = models.CharField(max_length = 255)
    title_xpath = models.CharField(max_length = 255)
    tagline_xpath = models.CharField(max_length = 255)
    link_xpath = models.CharField(max_length = 255)
    cost_xpath = models.CharField(max_length = 255)
