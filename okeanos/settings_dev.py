"""
Django settings for okeanos project.

Generated by 'django-admin startproject' using Django 1.11.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/


$ env1/bin/pip freeze > requirements.txt
$ env2/bin/pip install -r requirements.txt

pip freeze | xargs pip uninstall -y # delete libraries in virtualenv

django-admin.py makemessages -l en
and
python manage.py compilemessages
"""

import os
from django.utils.translation import ugettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.dirname(__file__)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5b4d^+px31d8-uf@m3c^b-0m%9jdgikybw#+a$-!@_z!1_y#@%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [u'127.0.0.1', u'okeanos.tucodigo.cl', u'localhost']

# Application definition

INSTALLED_APPS = [
    # 'material.theme.bluegrey',
    # 'material',
    # 'material.admin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'django.contrib.humanize',
    'easy_thumbnails',
    'ckeditor',
    'contact.apps.ContactConfig',
    'blog.apps.BlogConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'okeanos.urls'

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
                'django.template.context_processors.i18n',
                # 'material.frontend.context_processors.modules',
                'django.template.context_processors.media',
            ],
            'debug': True,
        },
    },
]

WSGI_APPLICATION = 'okeanos.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'es'
ugettext = lambda s: s

LANGUAGES = [
    ('en', _('English')),
    ('es', _('Spanish')),
]

TIME_ZONE = 'America/Santiago'
USE_I18N = True
USE_L10N = True
USE_TZ = True

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_ROOT = ('/home/tucodigo/webapps/static_okeanos')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    '/home/tucodigo/src/static_okeanos',
]

CKEDITOR_UPLOAD_PATH = "upload/"
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            ['Table', 'HorizontalRule', 'Smiley', 'SpecialChar'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter',
             'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink'],

            ['RemoveFormat', 'Source']
        ]
    }
}

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join('media').replace('\\', '/')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# for easy thumbnail
THUMBNAIL_ALIASES = {
    '': {
        'slider-img': {'size': (1265, 450), 'crop': True},
        'detalle-miniatura': {'size': (600, 400), 'crop': True},
        'card-img': {'size': (300, 150), 'crop': True},
    },
}

LOCALE_PATH = (os.path.join(BASE_DIR, "demoapp", "locale"))

# proaus hola@proaus proausemail
ADMINS = (('Hernan', 'hernan@tucodigo.cl'))
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST = 'smtp.webfaction.com'
EMAIL_HOST_USER = 'noresponder_tucodigo'
EMAIL_HOST_PASSWORD = '123prueba'
# EMAIL_SSL_KEYFILE = None
DEFAULT_FROM_EMAIL = 'prueba@tucodigo.cl'
# SERVER_EMAIL = 'HOLA@EMAIL.CL'
# DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
