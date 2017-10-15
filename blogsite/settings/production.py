import dj_database_url
import os
from .base import *

DEBUG = False
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
SECRET_KEY = os.environ.get('SECRET_KEY', 'asdfasdf')

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
