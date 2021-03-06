"""
Django settings for portfolio project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'n)g@v)@#d17n-1(@ysapejb_lue$*x5u8qo*as9vh(5^^7dva4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['jamesonspiff.pythonanywhere.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'portfolio_list',
    'django_hide',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_hide.middleware.CSRFHIDEMiddleware',
    'csp.middleware.CSPMiddleware',
]

ROOT_URLCONF = 'portfolio.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'portfolio.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


#Security tests
SECURE_HSTS_SECONDS = 3600  #increase the time 3600 = 1hour
SECURE_HSTS_INCLUDE_SUBDOMAINS = True   #to include subdomains

#CSP
CSP_DEFAULT_SRC = ["'self'", '*.mozilla.net', '*.mozilla.org', '*.mozilla.com']
CSP_STYLE_SRC = CSP_DEFAULT_SRC + ["'self'", "stackpath.bootstrapcdn.com"]

CSP_SCRIPT_SRC = CSP_DEFAULT_SRC + ["'self'", 
    "ajax.cloudflare.com", 
    "static.cloudflareinsights.com", 
    "www.google-analytics.com", 
    "ssl.google-analytics.com", 
    "cdn.ampproject.org", 
    "www.googletagservices.com", 
    "use.fontawesome.com",
    "pagead2.googlesyndication.com"]
   
# images from our domain and other domains
CSP_IMG_SRC = CSP_DEFAULT_SRC + ["'self'", 
    "www.google-analytics.com", 
    "raw.githubusercontent.com", 
    "googleads.g.doubleclick.net"]

# loading manifest, workers, frames, etc
CSP_FONT_SRC = ("'self'", 'fonts.googleapis.com')
CSP_CONNECT_SRC = ("'self'",  
    "www.google-analytics.com" )
CSP_OBJECT_SRC = ("'self'", )
CSP_BASE_URI = ("'self'", )
CSP_FRAME_ANCESTORS = ("'self'", )
CSP_FORM_ACTION = ("'self'", )
CSP_INCLUDE_NONCE_IN = ('script-src', )
CSP_MANIFEST_SRC = ("'self'", )
CSP_WORKER_SRC = ("'self'", )
CSP_MEDIA_SRC = ("'self'", )


try:
    from .local_settings import *
except ImportError:
    print("No local file you must be on production")
