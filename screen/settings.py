# coding=utf-8
import sys, os

APP_BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEBUG = any((cmd in sys.argv for cmd in ('runserver', 'shell', 'dbshell', 'sql', 'sqlall'))) \
    or os.environ.get('DEBUG', False)

if APP_BASEDIR not in sys.path:
    sys.path.insert(0, APP_BASEDIR)

SECRET_KEY = '1ed5(ru*y4$^i4&h5*g5$6suvz8xne=)0ldu)tear$+ni7!-%r'
APP_MODULE = 'screen'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


GOOGLE_ANALYTICS = 'UA-xxxxxxx-xx'

ADMINS = (
    (u'Simon Schmid', 'ssc@feinheit.ch'),
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

MEDIA_ROOT = os.path.join(APP_BASEDIR, 'upload')
MEDIA_URL = os.environ.get('MEDIA_URL', '/upload/')

STATIC_ROOT = os.path.join(APP_BASEDIR, 'static')
STATIC_URL = os.environ.get('STATIC_URL', '/static/')

print "STATIC_URL + %s, MEDIA URL + %s" % (STATIC_URL, MEDIA_URL)

# only use s3 on production
if all((var in os.environ for var in ('AWS_ACCESS_KEY_ID', 'AWS_SECRET_ACCESS_KEY', 'AWS_STORAGE_BUCKET_NAME'))):
    DEFAULT_FILE_STORAGE = 'screen.s3utils.MediaRootS3BotoStorage'
    STATICFILES_STORAGE = 'screen.s3utils.StaticRootS3BotoStorage'
    AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
    AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
    AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
    AWS_PRELOAD_METADATA = True

print "x STATIC_URL + %s, MEDIA URL + %s" % (STATIC_URL, MEDIA_URL)

TEMPLATE_LOADERS = (
    #'feinheit.mobile.template_loaders.MobileLoader',  # Activate this loader, the middleware and the context processor if you have specific mobile templates.
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
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
)

ROOT_URLCONF = APP_MODULE+'.urls'

TEMPLATE_DIRS = (
    os.path.join(APP_BASEDIR, APP_MODULE, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'fhadmin',
    APP_MODULE,

    'feincms',
    'feincms.module.medialibrary',
    'feincms.module.page',
    'mptt',

    'feincms_oembed',
    'gunicorn',
)

LANGUAGES = (
    ('de', 'German'),
    #('fr', 'French'),
    #('en', 'English'),
)

FEINCMS_ADMIN_MEDIA = '/static/feincms/'
TINYMCE_JS_URL = '/media/lib/tiny_mce/tiny_mce.js'
FEINCMS_RICHTEXT_INIT_CONTEXT  = {
    'TINYMCE_JS_URL': TINYMCE_JS_URL,
    'TINYMCE_CONTENT_CSS_URL': None,
    'TINYMCE_LINK_LIST_URL': None
}


SERVER_EMAIL = 'root@oekohosting.ch'
DEFAULT_FROM_EMAIL = 'root@oekohosting.ch'

COMPRESS_OUTPUT_DIR = 'cache'
COMPRESS_CSS_FILTERS = ['compressor.filters.css_default.CssAbsoluteFilter',
                        'compressor.filters.cssmin.CSSMinFilter']

import dj_database_url
DATABASES = {'default': dj_database_url.config(default='sqlite:///%s' % os.path.join(APP_BASEDIR, 'db.sqlite') )}
