from .base import *
from environ import environ

import sys


TESTING = len(sys.argv) > 1 and sys.argv[1] == 'test'

DEBUG = True

ALLOWED_HOSTS = ['*']

if DEBUG:
    if not TESTING:
        INSTALLED_APPS += ['debug_toolbar']
        MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']
        INTERNAL_IPS = ['127.0.0.1', 'localhost']
        DEBUG_TOOLBAR_PANELS = [
            'debug_toolbar.panels.versions.VersionsPanel',
            'debug_toolbar.panels.timer.TimerPanel',
            'debug_toolbar.panels.settings.SettingsPanel',
            'debug_toolbar.panels.headers.HeadersPanel',
            'debug_toolbar.panels.request.RequestPanel',
            'debug_toolbar.panels.sql.SQLPanel',
            'debug_toolbar.panels.staticfiles.StaticFilesPanel',
            'debug_toolbar.panels.templates.TemplatesPanel',
            'debug_toolbar.panels.cache.CachePanel',
            'debug_toolbar.panels.signals.SignalsPanel',
            'debug_toolbar.panels.logging.LoggingPanel',
            'debug_toolbar.panels.redirects.RedirectsPanel',
        ]
        DEBUG_TOOLBAR_CONFIG = {
            'INTERCEPT_REDIRECTS': False,
            'SHOW_TOOLBAR_CALLBACK': lambda request: True,
        }


if os.getenv('GITHUB_WORKFLOW'):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'postgres',
            'USER': 'postgres',
            'PASSWORD': 'postgres',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    SECRET_KEY = os.getenv('SECRET_KEY')
else:
    env = environ.Env()
    environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': env('DB_NAME'),
            'USER': env('DB_USER'),
            'PASSWORD': env('DB_PASSWORD'),
            'HOST': 'db',
            'PORT': 5432,
        }
    }
    SECRET_KEY = env('SECRET_KEY')