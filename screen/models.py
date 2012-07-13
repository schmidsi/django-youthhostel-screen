from django.db import models
from django.utils.translation import ugettext_lazy as _

from feincms.module.page.models import Page
from feincms.content.raw.models import RawContent
from feincms.content.richtext.models import RichTextContent
from feincms.content.template.models import TemplateContent
from feincms.content.medialibrary.models import MediaFileContent

from feincms_oembed.contents import OembedContent, FeedContent

from feincms_cleanse import cleanse_html

from contents import AnnouncementContent, SimpleGalleryContent, TextContent
from extensions import content_timing_extension

Page.register_templates({
    'title': 'Standard Screen',
    'path': 'screen.html',
    'regions': (
        ('main', _('Main content area')),
        ('ticker', _('News ticker'), 'inherited'),
        ('announcements', _('Announcements'), 'inherited'),
        ('inactive', _('Inactive')),
        ),
    })

content_timing_extension(RichTextContent, TextContent, MediaFileContent, OembedContent,
    SimpleGalleryContent, AnnouncementContent)

Page.register_extensions('changedate','navigation', 'ct_tracker')
Page.create_content_type(RichTextContent, regions=('main',), cleanse=cleanse_html)
Page.create_content_type(MediaFileContent, regions=('main',), POSITION_CHOICES=(('default', _('default')),))
Page.create_content_type(OembedContent, regions=('main',), TYPE_CHOICES=[
    ('default', _('default'), {'width' : 922, 'heigth' : 491, 'autoplay': 'true'})
])
Page.create_content_type(TextContent, regions=('main',))
Page.create_content_type(SimpleGalleryContent, regions=('main',))
Page.create_content_type(AnnouncementContent, regions=('announcements',))
Page.create_content_type(FeedContent, regions=('ticker',))
#Page.create_content_type(TemplateContent, regions=('main',))