import dj_database_url
import os
import mimetypes
from .base import *

mimetypes.add_type("text/css", ".css", True)
mimetypes.add_type("text/javascript", ".js", True)

DEBUG = os.environ.get('DJANGO_DEBUG', False) == 'True'
ALLOWED_HOSTS = ['*', 'jinyuz-blog.herokuapp.com']
SECRET_KEY = os.environ.get('SECRET_KEY', 'asdfasdf')

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

ADMINS = [
    ('Yujin', 'jinyuzprodigy@gmail.com'),
]

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'dev.jinyuz@gmail.com'
EMAIL_HOST_PASSWORD = '123523qwe'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
SERVER_EMAIL = EMAIL_HOST_USER


# AWS
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID', '')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = 'jinyuz-blog-static'
AWS_S3_CUSTOM_DOMAIN = '{bucket_name}.s3.amazonaws.com'.format(bucket_name=AWS_STORAGE_BUCKET_NAME)
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_LOCATION = 'static'
STATIC_URL = 'https://{custom_domain}/{location}'.format(custom_domain=AWS_S3_CUSTOM_DOMAIN, location=AWS_LOCATION)
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
