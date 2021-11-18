from . import rel   # , get_env_setting
import os
import ldap
from django_auth_ldap.config import LDAPSearch, MemberDNGroupType

# this is used if you want to have all apps in one directory
# the file apps.pth should contain a line like this:
# ./apps
#
# import site
# site.addpackage(rel(), "apps.pth", known_paths=set())

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['dcd62c7fd6d7.ngrok.io', '192.168.4.56', 'localhost', '127.0.0.1']

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

# import oauth2_provider.middleware.OAuth2TokenMiddleware
# import django.contrib.auth.middleware.AuthenticationMiddleware
MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "oauth2_provider.middleware.OAuth2TokenMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "corsheaders.middleware.CorsMiddleware",
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
    "whitenoise",
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
    "corsheaders",
    # Project apps
    "c_base_oauth2.apps.c_base_auth.apps.CBaseAuthConfig",
    "c_base_oauth2.apps.users.apps.UsersConfig",
    "oauth2_provider",
]

AUTH_USER_MODEL = "users.User"

LOGIN_URL = '/oauth/accounts/login/'
LOGIN_REDIRECT_URL = '/oauth/accounts/profile/'

WSGI_APPLICATION = "wsgi.application"

ROOT_URLCONF = "c_base_oauth2.urls"

SESSION_STORAGE = "django.contrib.sessions.backends.cached_db"
MESSAGE_STORAGE = "django.contrib.messages.storage.session.SessionStorage"

AUTHENTICATION_BACKENDS = [
    "oauth2_provider.backends.OAuth2Backend",
    "django.contrib.auth.backends.ModelBackend",
    # "account.auth_backends.EmailAuthenticationBackend",
    "django_auth_ldap.backend.LDAPBackend",
]

AUTH_LDAP_START_TLS = False   # default: True
AUTH_LDAP_SERVER_URI = "ldaps://dea.cbrp3.c-base.org/"

CBASE_BASE_DN = 'ou=crew,dc=c-base,dc=org'
AUTH_LDAP_CONNECTION_OPTIONS = {ldap.OPT_REFERRALS: 0}
# AUTH_LDAP_BIND_DN = ""
# AUTH_LDAP_BIND_PASSWORD = ""
# AUTH_LDAP_USER_DN_TEMPLATE = "uid=%(user)s,ou=crew,dc=c-base,dc=org" # necessary?
AUTH_LDAP_USER_SEARCH = LDAPSearch(
    "ou=crew,dc=c-base,dc=org", ldap.SCOPE_SUBTREE, "(uid=%(user)s)"
)
AUTH_LDAP_BIND_AS_AUTHENTICATING_USER = True
AUTH_LDAP_REQUIRE_GROUP = "cn=crew,ou=groups,dc=c-base,dc=org"
AUTH_LDAP_CACHE_GROUPS = True
AUTH_LDAP_GROUP_CACHE_TIMEOUT = 300
AUTH_LDAP_MIRROR_GROUPS = True
AUTH_LDAP_GROUP_TYPE = MemberDNGroupType('member')
AUTH_LDAP_GROUP_SEARCH = LDAPSearch(
    "ou=groups,dc=c-base,dc=org",
    ldap.SCOPE_SUBTREE,
    "(objectClass=groupOfNames)",
)

# AUTH_LDAP_USER_FLAGS_BY_GROUP = {
#    "is_member": "cn=crew,ou=groups,dc=c-base,dc=org",
#    "is_ldap_admin": "cn=ldap_admins,ou=groups,dc=c-base,dc=org",
#    "is_circle_member": "cn=circle,ou=groups,dc=c-base,dc=org",
#    "is_clab_member": "cn=cey-c-lab,ou=groups,dc=c-base,dc=org",
#    "is_cey_member": "cn=cey-schleuse,ou=groups,dc=c-base,dc=org",
#    "is_ceymaster": "cn=ceymaster,ou=groups,dc=c-base,dc=org",
# }

AUTH_LDAP_USER_ATTR_MAP = {
    "first_name": "givenName",
    "last_name": "sn",
    "email": "mail",
}

# Common app-specific settings
CORS_ORIGIN_ALLOW_ALL = True   # TODO: Correct this

OAUTH2_PROVIDER = {
    "OIDC_ENABLED": True,
    "OIDC_RSA_PRIVATE_KEY": os.environ.get("OIDC_RSA_PRIVATE_KEY"),
    'SCOPES': {
        # Scope needed for OIDC
        'openid': 'Use OpenID Connect.',
        # My scopes
        'membership': 'See you membership status and your crew name.',
        'email': 'See your e-mail address (e.g. {crew-name}@c-base.org).',
        'groups': 'See if your LDAP groups (e.g. "soundlab", "c-lab", "cey").',
        'realname': 'See your real name (CN).',
    },
    # These are the scopes used when the request comes
    # from a user directly accessing a protected resource
    # instead of a third-party service.
    # 'DEFAULT_SCOPES': ['membership', 'groups', 'email', 'realname'],
}

from .common.logs import LOGGING   # noqa: F401, E402
