from django.shortcuts import render
from django.template.response import TemplateResponse
from .models import EventEntry

# Create your views here.

def events_view(request):
    template_name = 'events.html'

    return TemplateResponse(request, template_name, {
        'events': EventEntry.objects.all()
        })
