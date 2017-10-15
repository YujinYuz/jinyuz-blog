from .base import *
import dj_database_url
from dj_database_url import config

DEBUG = False
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

DATABASES = {
    'default': dj_database_url.config(
        default=config
    )
}
