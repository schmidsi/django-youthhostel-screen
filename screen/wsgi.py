import os
import sys
import site

webapp_dir = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.abspath(os.path.join(webapp_dir, os.path.pardir))

if PATH not in sys.path:
    sys.path.insert(0, PATH)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "screen.settings")

site.addsitedir(os.path.join(
    PATH, 'lib', 'python%s' % sys.version[:3], 'site-packages'))

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()