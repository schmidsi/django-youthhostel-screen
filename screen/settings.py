# coding=utf-8
import sys, os

APP_BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if APP_BASEDIR not in sys.path:
    sys.path.insert(0, APP_BASEDIR)

execfile(os.path.join(APP_BASEDIR, 'secrets.py'))

LOGGING = {
    'version' : 1,
    'formatters' : {
        'console' : {
            'format' : '%(levelname)s %(message)s'
        },
        'file' : {
            'format' : '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        }
    },
    'handlers' : {
        'console' : {
            'level' : 'DEBUG',
            'class' : 'logging.StreamHandler',
            'formatter' : 'console'
        },
        'file' : {
            'level' : 'INFO',
            'class' : 'logging.handlers.RotatingFileHandler',
            'formatter' : 'file',
            'filename' : os.path.join(APP_BASEDIR, 'log/%s.log' % APP_MODULE),
            'maxBytes' : 1000000,
            'backupCount' : 10,
        },
            'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        }
    },
    'loggers': {
        '' : {
            'handlers': ['file', 'mail_admins'],
            'propagate' : True,
            'level' : 'INFO',
        },
    },
}

if 'runserver' in sys.argv:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    LOCAL_DEV = True
    DEBUG = True
    """
    LOGGING['loggers'].update({
        '' : {
            'handlers': ['console'],
            'propagate' : True,
            'level' : 'DEBUG',
        }})
    """
else:
    LOCAL_DEV = False
    DEBUG = True


GOOGLE_ANALYTICS = 'UA-xxxxxxx-xx'

ADMINS = (
    (u'FEINHEIT Developers', 'dev@feinheit.ch'),
    #(u'Matthias Kestenholz', 'mk@feinheit.ch'),
    #(u'Stefan Reinhard', 'sr@feinheit.ch'),
    #(u'Simon Schürpf', 'ss@feinheit.ch'),
    (u'Simon Schmid', 'ssc@feinheit.ch'),
    #(u'Simon Bächler', 'sb@feinheit.ch'),
)
MANAGERS = ADMINS
CONTACT_FORM_EMAIL = [mail for name, mail in ADMINS]

MAIN_DEVELOPER = None

if MAIN_DEVELOPER:
    ADMINS = ADMINS + (
        ('Main developer', MAIN_DEVELOPER),
        )

INTERNAL_IPS= ('212.243.229.34', '127.0.0.1')

TEMPLATE_DEBUG = DEBUG

TIME_ZONE = 'Europe/Zurich'
LANGUAGE_CODE = 'de-ch'
SITE_ID = 1
USE_I18N = True
USE_L10N = True

MEDIA_ROOT = os.path.join(APP_BASEDIR, 'media')
MEDIA_URL = '/media/'

ADMIN_MEDIA_PREFIX = '/static/admin/'
STATIC_ROOT = os.path.join(APP_BASEDIR, 'static')
STATIC_URL = '/static/'

SENTRY_REMOTE_URL = 'http://monitor.feinheit.ch/sentry/store/'

DEFAULT_FILE_STORAGE = 'feinheit.storage.SlugifyStorage'

TEMPLATE_LOADERS = (
    #'feinheit.mobile.template_loaders.MobileLoader',  # Activate this loader, the middleware and the context processor if you have specific mobile templates.
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

if not DEBUG and False: # Do not activate this by default
    # Use cached template loader
    # http://docs.djangoproject.com/en/dev/ref/templates/api/#loader-types
    TEMPLATE_LOADERS = (
        ('django.template.loaders.cached.Loader', (
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        )),
    )

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    #'feinheit.middleware.UserBasedExceptionMiddleware',
    #'feinheit.middleware.SpacelessMiddleware',
    #'feinheit.middleware.ThreadLocals',
    #'feinheit.mobile.middleware.RequestMiddleware',
    #'feinheit.middleware.AutoTemplateFallback',
    #'feinheit.middleware.ForceDomainMiddleware',
    #'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',

    'django.middleware.locale.LocaleMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.core.context_processors.static',
    #'feinheit.context_processors.meta_page',
    #'feinheit.context_processors.google_analytics',
    #'feinheit.mobile.context_processors.mobile_browser',
)

ROOT_URLCONF = APP_MODULE+'.urls'

TEMPLATE_DIRS = (
    os.path.join(APP_BASEDIR, APP_MODULE, 'templates'),
    os.path.join(APP_BASEDIR, 'feinheit', 'templates'),
)

INSTALLED_APPS = (
    #'feinheit.punctuated_slugs', # Allows . , : ; in slugs
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    #'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    #'sentry.client',
    #'compressor',
    'feinheit',
    #'feinheit.contextadmin',
    'feinheit.external',
    'fhadmin',
    #'feinheit.gallery',
    #'feinheit.newsletter',
    #'feinheit.sharing',
    #'feinheit.links',
    #'feinheit.agenda',
    #'form_designer',

    #'elephantblog',
    #'pinging',
    #'disqus',

    APP_MODULE,

    'feincms',
    'feincms.module.medialibrary',
    'feincms.module.page',
    'mptt',
    #'rosetta',


    #'django.contrib.comments',
)

LANGUAGES = (
    ('de', 'German'),
    #('fr', 'French'),
    #('en', 'English'),
)

FEINCMS_ADMIN_MEDIA = '/static/feincms/'
TINYMCE_JS_URL = '/static/tinymce/tiny_mce.js'
FEINCMS_RICHTEXT_INIT_CONTEXT  = {
    'TINYMCE_JS_URL': TINYMCE_JS_URL,
    'TINYMCE_CONTENT_CSS_URL': None,
    'TINYMCE_LINK_LIST_URL': None
}

GRID = {'column': 30, 'spacing': 10, 'vertical': 18}

""" Set this to the correct name: """
#PINGING_WEBLOG_NAME = 'Mein grossartiger Blog!'
#PINGING_WEBLOG_URL = 'http://www.feinheit.ch/blog'

SERVER_EMAIL = 'root@oekohosting.ch'
DEFAULT_FROM_EMAIL = 'root@oekohosting.ch'

COMPRESS_OUTPUT_DIR = 'cache'
COMPRESS_CSS_FILTERS = ['compressor.filters.css_default.CssAbsoluteFilter',
                        'compressor.filters.cssmin.CSSMinFilter']

CACHE_BACKEND = 'memcached://127.0.0.1:11211/'
CACHE_KEY_PREFIX = APP_MODULE
CACHE_MIDDLEWARE_SECONDS = 5 * 60
CACHE_MIDDLEWARE_KEY_PREFIX = APP_MODULE
CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True
