import json
import logging.config
from os import getenv
from os.path import dirname, abspath, join

################
##### SITE #####
################

PROJECT_DIR = dirname(dirname(abspath(__file__)))

SITE_ID = 1
SITENAME = 'truteordare'
SITEURL = 'http://localhost:8000/'

ROOT_URLCONF = 'website.urls'
WSGI_APPLICATION = 'website.wsgi.application'

ALLOWED_HOSTS = getenv('DJANGO_ALLOWED_HOSTS').split(',')
SECRET_KEY = getenv('DJANGO_SECRET_KEY')
DEBUG = getenv('DJANGO_DEBUG')

###################
##### LOGGING #####
###################

LOGLEVEL = getenv('DJANGO_LOGLEVEL')

logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            'format': '%(asctime)s %(levelname)s [%(name)s:%(lineno)s] %(module)s %(process)d %(thread)d %(message)s',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'console',
        },
    },
    'loggers': {
        '': {
            'level': LOGLEVEL,
            'handlers': ['console', ],
        },
    },
})

##################################
##### APPLICATION DEFINITION #####
##################################

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [join(PROJECT_DIR, 'templates')],
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

DATABASES = {
    'default': {
        'ENGINE': getenv('DATABASE_ENGINE', ''),
        'NAME': getenv('DATABASE_NAME', ''),
        'USER': getenv('DATABASE_USERNAME', ''),
        'PASSWORD': getenv('DATABASE_PASSWORD', ''),
        'HOST': getenv('DATABASE_HOST', ''),
        'PORT': getenv('DATABASE_PORT', ''),
        'OPTIONS': json.loads(
            getenv('DATABASE_OPTIONS', '{}')
        ),
        'TEST': {
            'NAME': 'travis_ci_test',
        }
    }
}

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

################################
##### INTERNATIONALIZATION #####
################################

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

########################
##### STATIC FILES #####
########################

STATIC_URL = '/static/'

################################
##### WEBSITE APPLICATIONS #####
################################

PACKAGE_APPS = [
    'markdownx',
]

WEB_APPS = [
    'blog',
]

INSTALLED_APPS += PACKAGE_APPS
INSTALLED_APPS += WEB_APPS

#################
##### OTHER #####
#################

blogname = 'TruteOrDare'
