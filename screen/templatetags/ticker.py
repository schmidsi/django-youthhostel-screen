from django import template

register = template.Library()

from screen.views import ticker_combined

register.simple_tag(ticker_combined)
