# -*- coding: utf-8 -*-

from django.db import models
from django.template.loader import render_to_string


class AnnouncementContent(models.Model):
    announcement = models.CharField('Announcement', max_length=200)
    
    class Meta:
        abstract = True
        verbose_name = u'Ankündigung'
        verbose_name_plural = u'Ankündigungen'
    
    def render(self, **kwargs):
        return self.announcement
