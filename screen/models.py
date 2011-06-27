from django.db import models
from django.utils.translation import ugettext_lazy as _

from feincms.module.page.models import Page
from feincms.content.raw.models import RawContent
from feincms.content.richtext.models import RichTextContent
from feincms.content.template.models import TemplateContent
from feincms.content.medialibrary.models import MediaFileContent

from feinheit.external.contents import OembedContent

Page.register_templates({
    'title': 'Standard Screen',
    'path': 'screen.html',
    'regions': (
        ('main', _('Main content area')),
        ('ticker', _('News ticker'), 'inherited'),
        ('announcements', _('Announcements'), 'inherited'),
        ),
    })

Page.register_extensions('changedate','navigation', 'ct_tracker')
Page.create_content_type(RichTextContent, regions=('main',), cleanse=False)
Page.create_content_type(MediaFileContent, POSITION_CHOICES=(('default', _('default')),))
Page.create_content_type(OembedContent, regions=('main',))
Page.create_content_type(TemplateContent, regions=('main', 'ticker', 'announcements',))
Page.create_content_type(RawContent, regions=('main',))