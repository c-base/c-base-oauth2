from . import rel   # , get_env_setting

# this is used if you want to have all apps in one directory
# the file apps.pth should contain a line like this:
# ./apps
#
# import site
# site.addpackage(rel(), "apps.pth", known_paths=set())

DEBUG = False
TEMPLATE_DEBUG = DEBUG

TIME_ZONE = "UTC"
LANGUAGE_CODE = "en-us"
SITE_ID = 1

USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_ROOT = rel("..", "static_collected")

STATICFILES_DIRS = [
    rel("static")
]

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    # "compressor.finders.CompressorFinder",
]

TEMPLATE_LOADERS = [
    "django.template.loaders.filesystem.Loader",
    "django.template.loaders.app_directories.Loader",
    # "django.template.loaders.eggs.Loader",
]

TEMPLATE_DIRS = [
    rel("templates"),
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': TEMPLATE_DIRS,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.template.context_processors.request",
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

MIDDLEWARE = [
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    # "django.middleware.http.ConditionalGetMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # Cookie-based, for anonymous users
    "django.middleware.locale.LocaleMiddleware",
    # "account.middleware.LocaleMiddleware",
    # Account-based, for registered users
    # "account.middleware.TimezoneMiddleware",
]

INSTALLED_APPS = [
    # Django apps
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.humanize",
    "django.contrib.messages",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.staticfiles",
    "django.contrib.admin",

    # Pinax user accounts apps
    # "account",
    # "pinax_theme_bootstrap_account",
    # "django_forms_bootstrap",
    # TODO: bootstrap/field.html template collides with crispy-forms
    
    # Top utilities for assets management, db migrations, api and more
    # "compressor",
    # "crispy_forms",
    # "django_extensions",
    # "infinite_pagination",
    # #"imagekit",
    # "rest_framework",
    # "south",
    # "storages",
    "oauth2_provider",
    # Project apps
    "c_base_oauth2.apps.c_base_auth.apps.CBaseAuthConfig",
    "c_base_oauth2.apps.users.apps.UsersConfig",
]

AUTH_USER_MODEL = "users.User"

LOGIN_URL='/admin/login/'

WSGI_APPLICATION = "wsgi.application"

ROOT_URLCONF = "c_base_oauth2.urls"

SESSION_STORAGE = "django.contrib.sessions.backends.cached_db"
MESSAGE_STORAGE = "django.contrib.messages.storage.session.SessionStorage"

AUTHENTICATION_BACKENDS = [
    # "account.auth_backends.EmailAuthenticationBackend",
    "django.contrib.auth.backends.ModelBackend",
]

# Common app-specific settings

from .common.logs import LOGGING   # noqa: F401, E402
