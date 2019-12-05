"""
Django settings for apimanager project.

Generated by 'django-admin startproject' using Django 1.10.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

from django.core.exceptions import ImproperlyConfigured
from django.urls import reverse_lazy


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = None

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Set this to e.g. ['127.0.0.1', 'localhost'] if DEBUG = False
ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap3',
    'bootstrap_datepicker_plus',
    'mathfilters',

    'base',
    'obp',
    'consumers',
    'users',
    'branches',
    'entitlementrequests',
    'customers',
    'metrics',
    'config',
    'webui',
    'methodrouting',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'apimanager.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'base.context_processors.api_root',
                'base.context_processors.api_username',
                'base.context_processors.api_user_id',
                'base.context_processors.api_tester_url',
            ],
        },
    },
]

WSGI_APPLICATION = 'apimanager.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '..', '..', 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # noqa
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-gb'

TIME_ZONE = 'Europe/Berlin'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

# Set this to your local directory for static files
STATIC_ROOT = os.path.join(BASE_DIR, '..', '..', 'static-collected')


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
         },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'mail_admins'],
            'level': 'INFO',
        },
        'base': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        'obp': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        'consumers': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        'users': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        'customers': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        'metrics': {
            'handlers': ['console'],
            'level': 'INFO',
        },
    },
}


LOGIN_URL = reverse_lazy('home')

#Map Java: yyyy-MM-dd'T'HH:mm'Z'
API_DATETIMEFORMAT = '%Y-%m-%dT%H:%M:%SZ'
#Map Java: yyyy-MM-dd'T'HH:mm:ss.SSS'Z'
API_DATEFORMAT = '%Y-%m-%dT%H:%M:%S.%fZ'


API_HOST = 'http://127.0.0.1:8080'
API_BASE_PATH = '/obp/v'
API_VERSION = '3.1.0'

# URL to API Tester if it is running on API_HOST
API_TESTER_URL = ''

# Always save session$
SESSION_SAVE_EVERY_REQUEST = True

# Paths on API_HOST to OAuth
OAUTH_TOKEN_PATH = '/oauth/initiate'
OAUTH_AUTHORIZATION_PATH = '/oauth/authorize'
OAUTH_ACCESS_TOKEN_PATH = '/oauth/token'

# Set OAuth client key/secret in apimanager/local_settings.py
OAUTH_CONSUMER_KEY = None
OAUTH_CONSUMER_SECRET = None

# Path on API_HOST to DirectLogin
DIRECTLOGIN_PATH = '/my/logins/direct'

# Set to true if the API is connected to a core banking system
GATEWAYLOGIN_HAS_CBS = False



CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': 'unix:/tmp/memcached.sock',
    }
}

# Use BOOTSTRAP3 if you are using Bootstrap 3
BOOTSTRAP4 = {
    'include_jquery': True,
}

# Apps to exclude when request to OBP-API's api
EXCLUDE_APPS = []
# Functions to exclude when request to OBP-API's api
EXCLUDE_FUNCTIONS = []
# Url Patterns to exclude when reqeust to OBP-API's api
EXCLUDE_URL_PATTERN = []
# App Name to aggregate metrics
API_EXPLORER_APP_NAME = 'xxx'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    }
}
CACHE_DATEFORMAT = '%Y%m%d%H%M%S'
CACHE_TIME = 3600

# Local settings can override anything in here
try:
    from apimanager.local_settings import *  # noqa
except ImportError:
    pass

# Settings here might use parts overwritten in local settings
API_ROOT = API_HOST + API_BASE_PATH + API_VERSION
# For some reason, swagger is not available at the latest API version
API_URL_SWAGGER = API_HOST + '/obp/v1.4.0/resource-docs/v' + API_VERSION + '/swagger'  # noqa

VERIFY = True if API_HOST.startswith("https") else False

if not OAUTH_CONSUMER_KEY:
    raise ImproperlyConfigured('Missing settings for OAUTH_CONSUMER_KEY')
if not OAUTH_CONSUMER_SECRET:
    raise ImproperlyConfigured('Missing settings for OAUTH_CONSUMER_SECRET')
