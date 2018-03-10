"""
Django settings for rental project.

Generated by 'django-admin startproject' using Django 1.11.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8$jwsqhgsvnvay21#ezp48$8-$+mam(a8$0&dp^qa2daiq$(5#'


ALLOWED_HOSTS = ['rental-ads.herokuapp.com']


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # third party apps go here
    'taggit',

    # local apps go here
    'accounts',
    'rentals',
    'profiles',
    'errors',
]

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# add this
import dj_database_url
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)
DATABASES['default']['CONN_MAX_AGE'] = 500

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.environ.get('DATABASE_NAME'),
#         'USER': os.environ.get('DATABASE_USER'),
#         'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
#         'HOST': os.environ.get('DATABASE_HOST'),
#         'PORT': os.environ.get('DATABASE_PORT'),
#     }
# }



STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'


CORS_REPLACE_HTTPS_REFERER      = True
HOST_SCHEME                     = "https://"
SECURE_PROXY_SSL_HEADER         = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT             = True
SESSION_COOKIE_SECURE           = True
CSRF_COOKIE_SECURE              = True
SECURE_HSTS_INCLUDE_SUBDOMAINS  = True
SECURE_HSTS_SECONDS             = 1000000
SECURE_FRAME_DENY               = True



B2_BUCKET_NAME = os.environ.get('B2_BUCKET_NAME')
B2_BUCKET_ID = os.environ.get('B2_BUCKET_ID')
B2_ACCOUNT_ID = os.environ.get('B2_ACCOUNT_ID')
B2_APPLICATION_KEY = os.environ.get('B2_APP_KEY')
DEFAULT_FILE_STORAGE = 'django_b2storage.backblaze_b2.B2Storage' # To be able to use B2



#For email verification
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'ajaykarki619'
EMAIL_HOST_PASSWORD = 'gmail_12371'
