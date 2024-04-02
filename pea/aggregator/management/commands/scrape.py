from lxml import html
import requests
from datetime import datetime
from models import EventEntry, XpathImporter

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'}


for xi in XpathImporter.objects.all():

    r = requests.get(xi.url, headers = headers)

    event_elements = html.fromstring(r.content)

    for ee in event_elements:
        if xi.title_path:
            title = ee.xpath(xi.title_xpath)[0].text
        if xi.date_xpath:
            date = ee.xpath(xi.date_xpath)[0].text
        if xi.time.xpath:
            time = ee.xpath(xi.time_xpath)[0].text
        if xi.tagline.xpath:
            tagline = ee.xpath(xi.tagline_xpath)[0].text
        if xi.link_xpath:
            link = ee.xpath(xi.link_xpath)[0].text
        if xi.location_xpath:
            location = ee.xpath(xi.location_xpath)[0].text


        formatted_date = datetime.strptime(date, xi.date_format)
        formatted_time = datetime.strtime(time, xi.time_format)
        new_event = EventEntry(title = title, tagline = tagline, date = formatted_date, \
                time = formatted_time, link = link, location = location, cost = cost)
        new_event.save()
