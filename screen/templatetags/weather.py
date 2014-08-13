import json

from datetime import datetime

from django import template
from django.conf import settings
from django.core.exceptions import ValidationError

from feincms_oembed.models import CachedLookup

register = template.Library()


ICON_MAP = {
    'clear-day': 'wi-day-sunny',
    'clear-night': 'wi-night-clear',
    'rain': 'wi-rain',
    'snow': 'wi-snow',
    'sleet': 'wi-rain-mix',
    'wind': 'wi-windy',
    'fog': 'wi-fog',
    'cloudy': 'wi-cloudy',
    'partly-cloudy-day': 'wi-day-cloudy',
    'partly-cloudy-night': 'wi-night-cloudy'
}

@register.inclusion_tag('widgets/weather.html', takes_context=True)
def weather_widget(context, lat, lng, units, lang, exclude):
    url = 'https://api.forecast.io/forecast/%(key)s/%(lat)s,%(lng)s?units=%(units)s&lang=%(lang)s&exclude=%(exclude)s' % {
        'key': settings.FORECAST_IO_API_KEY,
        'lat': lat,
        'lng': lng,
        'units': units or 'ca',
        'lang': lang or 'en',
        'exclude': exclude or ""
    }

    raw = CachedLookup.objects.request(url, max_age=10*60)
    parsed = json.loads(raw)

    weather = {
        'current': {
            'temp': int(round(parsed['currently']['temperature'])),
            'icon': icon_lookup(parsed['currently']['icon']),
            'humidity': parsed['currently']['humidity']
        },
        'forecast': [],
    }

    for forecast in parsed['daily']['data']:
        weather['forecast'].append({
            'day': datetime.fromtimestamp(forecast['time']).strftime('%a'),
            'high': int(round(forecast['temperatureMax'])),
            'low': int(round(forecast['temperatureMin'])),
            'icon': icon_lookup(forecast['icon']),
        })

    context['weather'] = weather

    return context


def icon_lookup(icon):
    if ICON_MAP.has_key(icon):
        return ICON_MAP[icon]
    else:
        return 'wi-alien'
