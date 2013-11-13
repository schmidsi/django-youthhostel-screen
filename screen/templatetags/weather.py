from django import template
from django.core.exceptions import ValidationError

from feincms_oembed.models import CachedLookup

from lxml import etree

register = template.Library()


@register.inclusion_tag('widgets/weather.html', takes_context=True)
def weather_widget(context, city_search):
    try:
        raw = CachedLookup.objects.request('http://www.google.com/ig/api?weather=%s' % city_search, max_age=10*60)
        xmlroot = etree.XML(raw)
        xmlweather = xmlroot.find('weather')

        weather = {
            'current' : {
                'temp' : xmlweather.find('current_conditions').find('temp_c').attrib['data'],
                'icon' : xmlweather.find('current_conditions').find('icon').attrib['data'].split('/')[-1],
                'humidity' : xmlweather.find('current_conditions').find('humidity').attrib['data'].split(' ')[-1],
            },
            'forecast' : [],
        }

        for xmlforecast in xmlweather.findall('forecast_conditions'):
            weather['forecast'].append({
                'day' : xmlforecast.find('day_of_week').attrib['data'],
                'high' : (int(xmlforecast.find('high').attrib['data']) - 32) * 5 / 9,
                'low' : (int(xmlforecast.find('low').attrib['data']) - 32) * 5 / 9,
                'icon' : xmlforecast.find('icon').attrib['data'].split('/')[-1],
            })

        context['weather'] = weather
    except ValidationError:
        # if we cannot lookup weather, skip it
        pass

    return context