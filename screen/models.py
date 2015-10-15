from django.db import models
from django.utils.translation import ugettext_lazy as _

from feincms.module.page.models import Page
from feincms.module.medialibrary.models import MediaFile
from feincms.content.richtext.models import RichTextContent
from feincms.content.medialibrary.v2 import MediaFileContent

from feincms_oembed.contents import OembedContent, FeedContent

from mediavariations.contrib.feincms.extensions import variations

from contents import AnnouncementContent, SimpleGalleryContent, \
    TextContent, NewswallContent, FacebookImagePostsContent
from extensions import content_timing_extension, mediafile_cover_extension, \
    page_location

#MediaFile.register_extension(variations)
MediaFile.register_extension(mediafile_cover_extension)

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
    SimpleGalleryContent, AnnouncementContent, FacebookImagePostsContent)

Page.register_extensions(
    'feincms.module.extensions.changedate',
    'feincms.module.extensions.ct_tracker')

Page.register_extension(page_location)

#Page.create_content_type(RichTextContent, regions=('main',), cleanse=cleanse_html)
Page.create_content_type(MediaFileContent, regions=('main',), TYPE_CHOICES=(('default', _('default')),))
Page.create_content_type(OembedContent, regions=('main',), TYPE_CHOICES=[
    ('default', _('default'), {'width' : 922, 'heigth' : 491, 'autoplay': 'true'})
])
Page.create_content_type(TextContent, regions=('main',))
Page.create_content_type(SimpleGalleryContent, regions=('main',))
Page.create_content_type(FacebookImagePostsContent, regions=('main',))
Page.create_content_type(AnnouncementContent, regions=('announcements',))
Page.create_content_type(NewswallContent, regions=('ticker',))
#Page.create_content_type(TemplateContent, regions=('main',))