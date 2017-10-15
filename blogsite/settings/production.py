from .base import *
import dj_database_url
from dj_database_url import config

DEBUG = False
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
SECRET_KEY = config('SECRET_KEY')

DATABASES = {
    'default': dj_database_url.config(
        default=config
    )
}
