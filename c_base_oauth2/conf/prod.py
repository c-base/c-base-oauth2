# flake8: noqa
from .base import *
from . import get_env_setting

DEBUG = False
TEMPLATE_DEBUG = False

SECRET_KEY = get_env_setting("DJANGO_SECRET_KEY")

ADMINS = [
    ('Uwe Kamper', 'uk@c-base.org'),
]

ALLOWED_HOSTS = ['c-base.org', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase',
    }
}

# Configure site name and domain
DOMAIN_NAME = "c-base.org"
SITE_NAME = "c-base.org"

DEFAULT_FROM_EMAIL = "{} <hey@{}>".format(SITE_NAME, DOMAIN_NAME)
SERVER_EMAIL = "server@{}".format(DOMAIN_NAME)
EMAIL_SUBJECT_PREFIX = "[{}]".format(SITE_NAME)

# Database and cache settings
# DATABASES = herokuify.get_db_config()
# CACHES = herokuify.get_cache_config()

# Setup storage for static files and media using S3 Boto backend
# DEFAULT_FILE_STORAGE = "herokuify.storage.S3MediaStorage"
# STATICFILES_STORAGE = "herokuify.storage.CachedS3StaticStorage"
# COMPRESS_STORAGE = "herokuify.storage.CachedS3StaticStorage"
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_URL = '/oauth/static/'
STATIC_ROOT = '/home/oauth/c-base-oauth2/static_files/'

# MEDIA_URL = "https://{0}.s3.amazonaws.com/media/".format(AWS_STORAGE_BUCKET_NAME)
# STATIC_URL = "https://{0}.s3.amazonaws.com/static/".format(AWS_STORAGE_BUCKET_NAME)

AUTH_LDAP_SERVER_URI = "ldap://meridian.c-base.org/"
AUTH_LDAP_START_TLS = True

# OIDC_ISS_ENDPOINT = "https://c-base.org/oauth"
USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
