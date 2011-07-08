# -*- coding: utf-8 -*-

from django.conf import settings
from django.db import models


DEFAULT_DURATION = getattr('settings', 'SCREEN_DEFAULT_DURATION', 60)

def content_timing_extension(*content_classes):
    for cls in content_classes:
        cls.add_to_class('priority', models.PositiveIntegerField(default=1))
        
        cls.add_to_class('morning', models.BooleanField('Morgen (06:00-13:00)', default=True))
        cls.add_to_class('afternoon', models.BooleanField('Nachmittag (13:00-17:00)', default=True))
        cls.add_to_class('evening', models.BooleanField('Abend (17:00-23:00)', default=True))
        cls.add_to_class('night', models.BooleanField('Nacht (23:00-06:00)', default=True))
        
        cls.add_to_class('boost_start', models.TimeField('Vorzugzeit Start', blank=True, null=True))
        cls.add_to_class('boost_end', models.TimeField('Vorzugzeit Ende', blank=True, null=True))
        cls.add_to_class('boost_priority', models.PositiveIntegerField('Priorität in der Vorzugzeit', blank=True, null=True))
        
        cls.add_to_class('duration', models.PositiveIntegerField('Anzeigedauer (s)', default=DEFAULT_DURATION))