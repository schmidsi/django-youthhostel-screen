# -*- coding: utf-8 -*-

from django.conf import settings
from django.db import models

from feincms.admin.item_editor import FeinCMSInline


DEFAULT_DURATION = getattr(settings, 'SCREEN_DEFAULT_DURATION', 60)

def create_item_admin(model_fields):
    class ItemAdmin(FeinCMSInline):
        fields = (
            tuple(model_fields),
            ('priority', 'duration', 'morning', 'afternoon', 'evening', 'night'),
            ('boost_priority', 'boost_start', 'boost_end'),
            ('region', 'ordering')
        )
        raw_id_fields = ('mediafile',)

    return ItemAdmin

def content_timing_extension(*content_classes):
    for cls in content_classes:
        prefields = cls._meta.get_all_field_names()

        cls.add_to_class('priority', models.PositiveIntegerField(default=1))
        
        cls.add_to_class('morning', models.BooleanField('Morgen (06:00-10:00)', default=True))
        cls.add_to_class('afternoon', models.BooleanField('Nachmittag (10:00-13:30)', default=True))
        cls.add_to_class('evening', models.BooleanField('Abend (13:30-23:00)', default=True))
        cls.add_to_class('night', models.BooleanField('Nacht (23:00-06:00)', default=True))
        
        cls.add_to_class('boost_start', models.TimeField('Vorzugzeit Start', blank=True, null=True))
        cls.add_to_class('boost_end', models.TimeField('Vorzugzeit Ende', blank=True, null=True))
        cls.add_to_class('boost_priority', models.PositiveIntegerField('Priorität in der Vorzugzeit', blank=True, null=True))
        
        cls.add_to_class('duration', models.PositiveIntegerField('Anzeigedauer (s)', default=DEFAULT_DURATION))

        cls.add_to_class('feincms_item_editor_inline', create_item_admin(prefields))
