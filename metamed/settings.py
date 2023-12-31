"""
Django settings for metamed project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-p8j028^j53mvw6z*^=akodb2#f^1)an3z7@u%cl0db5hz9yd0&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1','phoenixhis.com','139.59.58.42','167.71.235.236',"localhost",'143.110.184.9']
STRIPE_PUBLISHABLE_KEY = 'pk_test_51MxUFkSI3RvJrBdpGBTgexZC4TdmVH0ZqhfXF8jaSIkhxWKTAGSR6Ss944SgYgyiY2JRLoKkmve1KQQ1bldxEUWa006X3Rs4xa'
STRIPE_SECRET_KEY = 'sk_test_51MxUFkSI3RvJrBdpm1QB3iy1dwwiC3OVe2PsANRA1OGycvIlxYHxxVUXpxbo8WC6AEfolbq3FzWA4pbgjlAfOq6p00fFlO0UA9'

AUTH_USER_MODEL = 'adminapp.CustomUser'
# Application definition
STATIC_URL = 'root/projectdir/metamedplus/static/'
STATICFILES_DIRS = [
   os.path.join(BASE_DIR, "static"),
 ]
STATIC_ROOT = '/root/projectdir/metamedplus/staticfiles'

INSTALLED_APPS = [
    "whitenoise.runserver_nostatic",
    'adminapp',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'clearcache',

    'django_seed',
    # 'channels',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'metamed.urls'



EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp-relay.brevo.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_USE_SSL = False
EMAIL_HOST_USER = 'programmer62563@gmail.com'
EMAIL_HOST_PASSWORD = 'CtYc9QV0yGR3fn7x'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), ],
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

WSGI_APPLICATION = 'metamed.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/


# STATICFILES_DIRS = [
#   os.path.join(BASE_DIR, "static"),
# ]


STATIC_URL = '/static/'
STATICFILES_DIRS = [
   os.path.join(BASE_DIR, "static"),
 ]


# STATICFILES_DIRS = (str(BASE_DIR.joinpath('static')),)
# STATIC_URL = '/static/'

# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'  
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# STATIC_ROOT = '/root/projectdir/metamedplus/metamed/static'


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


AUTHENTICATION_BACKENDS = (
        'django.contrib.auth.backends.ModelBackend',
    )

ASGI_APPLICATION = 'metamed.routing.application'

# Use Redis as the channel layer
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer"  # Use a production-ready layer in a real application.
    },
}