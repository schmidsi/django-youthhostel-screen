# -*- coding: utf-8 -*-
import re

from django.db import models
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _

from feincms.module.medialibrary.models import Category

from feincms_oembed.contents import OembedContent as OriginalOembedContent

from newswall.models import Source


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
    size = models.CharField(max_length=6, choices=(
        ('small', 'small'),
        ('medium', 'medium'),
        ('large', 'large'),
    ), default='medium')

    feincms_item_editor_includes = {
        'head': ['admin/content/text/init.html'],
    }

    class Meta:
        abstract = True
        verbose_name = _('Text')
        verbose_name_plural = _('Texts')

    def render(self, **kwargs):
        return render_to_string('content/text/default.html', {'content' : self})


class NewswallContent(models.Model):
    sources = models.ManyToManyField(Source)

    class Meta:
        abstract = True
        verbose_name = _('News Panel')
        verbose_name_plural = _('News Panel')

    def render(self, **kwargs):
        return render_to_string('content/newswall/default.html', {'content' : self})


class FacebookImagePostsContent(models.Model):
    user = models.CharField(max_length=100, default="youthhostel.ch", help_text="Username of the Facebookpage to get the Imageposts from")

    class Meta:
        abstract = True
        verbose_name = _('Facebook Image Posts')
        verbose_name_plural = _('External Image Posts')

    def render(self, **kwargs):
        return render_to_string('content/facebook/default.html', {'content' : self})


class WeatherContent(models.Model):
    location = models.CharField(max_length=100, blank=True, help_text="Falls leer wird der Ort der Seite genommen")

    class Meta:
        abstract = True
        verbose_name = _('Weather Panel')
        verbose_name_plural = _('Weather Panel')

    def render(self, **kwargs):
        return "RENDER IN FRONTEND"

