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
        verbose_name = _('Newswall')
        verbose_name_plural = _('Newswall')

    def render(self, **kwargs):
        return render_to_string('content/newswall/default.html', {'content' : self})


class OembedContent(OriginalOembedContent):
    """
    Adjust OembedContent to handle Youtube Embeds differently, to use the 
    Youtube Player API: https://developers.google.com/youtube/iframe_api_reference?hl=de
    """
    
    class Meta:
        abstract = True
        verbose_name = _('External content')
        verbose_name_plural = _('External contents')

    def render(self, **kwargs):
        if re.compile(r'youtube').search(self.url):
            id = re.search(r'([?&]v=|./././)([^#&]+)', self.url).group(2)
            return render_to_string('external/youtube.html', {'content': self, 'id': id})
        else:
            return self.get_html_from_json(fail_silently=True)

