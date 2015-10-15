# -*- coding: utf-8 -*-

from django.conf import settings
from django.db import models

from feincms.admin.item_editor import FeinCMSInline


DEFAULT_DURATION = getattr(settings, 'SCREEN_DEFAULT_DURATION', 60)


def create_item_admin(model_fields):
    class ItemAdmin(FeinCMSInline):
        fields = (
            tuple(model_fields),
            ('priority', 'duration', 'morning', 'noon', 'afternoon', 'evening', 'night'),
            ('region', 'ordering')
        )
        raw_id_fields = ('mediafile',)

    return ItemAdmin


def content_timing_extension(*content_classes):
    for cls in content_classes:
        prefields = cls._meta.get_all_field_names()

        cls.add_to_class('priority', models.PositiveIntegerField(default=1,
            choices=((1, 'Tief'), (2, 'Mittel'), (3, 'Hoch')) ))
        
        cls.add_to_class('morning', models.BooleanField('Morgen (06:00-10:00)', default=True))
        cls.add_to_class('noon', models.BooleanField('Mittag (10:00-13:30)', default=True))
        cls.add_to_class('afternoon', models.BooleanField('Nachmittag (13:30-17:00)', default=True))
        cls.add_to_class('evening', models.BooleanField('Abend (17:00-23:00)', default=True))
        cls.add_to_class('night', models.BooleanField('Nacht (23:00-06:00)', default=True))
        
        cls.add_to_class('duration', models.PositiveIntegerField('(Maximale) Anzeigedauer in Sekunden.', default=DEFAULT_DURATION))

        cls.add_to_class('feincms_item_editor_inline', create_item_admin(prefields))


def mediafile_cover_extension(cls, admin_cls):
    cls.add_to_class('cover', models.BooleanField('Vollbild (Bild kann beschnitten werden, nur anwenden bei Bildern ohne Texte am Rand', default=False))


def page_location(cls, admin_cls):
    cls.add_to_class('location', models.CharField('Standort (für Wetter)', max_length=100, default='Basel, Switzerland'))
