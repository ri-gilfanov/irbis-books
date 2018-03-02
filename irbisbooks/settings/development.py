from .base import *


DEBUG = True


# debug_toolbar

INSTALLED_APPS.extend([
    'debug_toolbar',
])

MIDDLEWARE.extend([
    'debug_toolbar.middleware.DebugToolbarMiddleware',
])

INTERNAL_IPS = ['127.0.0.1']
