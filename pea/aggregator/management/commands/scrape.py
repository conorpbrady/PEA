from lxml import html
import requests
from datetime import datetime
from aggregator.models import EventEntry, XpathImporter

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'}


for xi in XpathImporter.objects.all():

    r = requests.get(xi.url, headers = headers)

    tree = html.fromstring(r.content)
    event_elements = tree.xpath(xi.events_elements_xpath)
    title = ''
    tagline = ''
    link = ''
    location = ''
    cost = ''

    for ee in event_elements:
        if xi.title_xpath:
            title = ee.xpath(xi.title_xpath)[0].text.strip()
        if xi.date_xpath:
            date = ee.xpath(xi.date_xpath)[0].text.strip()
        if xi.time_xpath:
            time = ee.xpath(xi.time_xpath)[0].text.strip()
        if xi.tagline_xpath:
            tagline_elements = ee.xpath(xi.tagline_xpath)
            if tagline_elements:
                tagline = tagline_elements[0].text.strip()
        if xi.link_xpath:
            link = ee.xpath(xi.link_xpath)[0].text.strip()
        if xi.location_xpath:
            location = ee.xpath(xi.location_xpath)[0].text.strip()
        if xi.cost_xpath:
            cost_elements = ee.xpath(xi.cost_xpath)
            if cost_elements:
                cost = cost_elements[0].text.strip()

        # Gonna need to catch some inconsistencies in the date format
        # Could be Jan, Feb, June, July
        # Sep vs Sept
        try:
            formatted_date = datetime.strptime(date, xi.date_format)
        except ValueError:
            df = xi.date_format.replace('%b', '%B')
            formatted_date = datetime.strptime(date, df)
        # Gonna need to try and pad this, some times are 7pm others 9:45pm, etc
        # Multiple time formats?
        # Custom time interpreter?
        try:
            formatted_time = datetime.strptime(time, xi.time_format).time()
        except ValueError:
            tf = xi.time_format
            p = tf.find("%I")
            new_tf = tf[:p+2] + ":%M" + tf[p+2:]
            formatted_time = datetime.strptime(time, new_tf).time()

        new_event = EventEntry(title = title, tagline = tagline, date = formatted_date, \
                time = formatted_time, link = link, location = location, cost = cost)
        new_event.save()
