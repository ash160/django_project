"""
Django settings for helo project.

Generated by 'django-admin startproject' using Django 3.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'a*^%#7!jb0k5f*_7d$^#b9oe08u1b^igh_v81%2p=23e%sl6-4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['3.129.89.120',
                 'incometaxlegalsala.com',
                 '127.0.0.1',]



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home',
    'storages',
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

ROOT_URLCONF = 'helo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'template')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'helo.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
'''
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'Legalsalah2021',
        'USER': 'Legal',
        'PASSWORD': 'Legalsalah2020',
        'HOST': 'legalsalah.cm1wy20rotdq.us-east-2.rds.amazonaws.com',
        'PORT': '5432',
    }
}
'''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'snjmbudd',
        'USER': 'snjmbudd',
        'PASSWORD': 'pxn_pmjvpmUH7cuyrwUZCEMDYS8mBW0R',
        'HOST': 'isilo.db.elephantsql.com',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/



'''
STATICFILES_DIRS=[
    os.path.join(BASE_DIR,'static')

]

STATIC_URL = '/static/'
STATICFILES_DIRS=[]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT=os.path.join(BASE_DIR,'media')

'''


USING_S3 = True


if USING_S3:
    # AWS SETTINGS
    AWS_ACCESS_KEY_ID = 'AKIATCML2ROCI75DOVYP'
    AWS_SECRET_ACCESS_KEY = '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'
    AWS_STORAGE_BUCKET_NAME = 'legalsalah2021'
    AWS_DEFAULT_ACL = 'public-read'
    AWS_S3_USE_SSL =False

    AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

    # AWS S3 static settings
    STATIC_FOLDER = 'static'
    STATIC_ROOT = 'media'


    STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, STATIC_FOLDER)
    STATICFILES_STORAGE = 'helo.default_storages.StaticStorage'

    # AWS S3 public media settings
    MEDIA_FOLDER = 'media'
    MEDIA_ROOT = 'media/'
    MEDIA_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, MEDIA_FOLDER)
    DEFAULT_FILE_STORAGE = 'helo.default_storages.MediaStorage'
else:
    # IF WE ARE WORKING LOCALLY WITHOUT AWS
    STATIC_URL = 'static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    MEDIA_URL = 'media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, MEDIA_URL)



