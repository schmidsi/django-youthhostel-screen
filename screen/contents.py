# -*- coding: utf-8 -*-

from django.db import models
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _
from feincms.module.medialibrary.models import Category

class AnnouncementContent(models.Model):
    announcement = models.CharField('Announcement', max_length=200)
    
    class Meta:
        abstract = True
        verbose_name = u'Ankündigung'
        verbose_name_plural = u'Ankündigungen'
    
    def render(self, **kwargs):
        return render_to_string('content/announcements/default.html', {'content' : self})


class SimpleGalleryContent(models.Model):
    category = models.ForeignKey(Category, help_text=_('Choose a feincms medialibrary category to display as gallery'))

    class Meta:
        abstract = True
        verbose_name = _('Simple image gallery')
        verbose_name_plural = _('Simple image galleries')

    def render(self, **kwargs):
        images = self.category.mediafile_set.filter(type='image')

        return render_to_string('content/simplegallery/default.html', {'content' : self, 'images' : images})


class TextContent(models.Model):
    text = models.TextField()

    class Meta:
        abstract = True
        verbose_name = _('Text')
        verbose_name_plural = _('Texts')

    def render(self, **kwargs):
        return render_to_string('content/text/default.html', {'content' : self})
