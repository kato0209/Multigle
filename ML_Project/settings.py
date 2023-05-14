"""
Django settings for ML_Project project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
import environ
from dotenv import load_dotenv
from decouple import config
from dj_database_url import parse as dburl

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

RENDER_DEPLOY = True
env = environ.Env()
if RENDER_DEPLOY:
    env.read_env('/etc/secrets/.env')
else:
    env.read_env(os.path.join(BASE_DIR,'.env'))
print(env('SECRET_KEY', default=False))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY', default=False)
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [env('ALLOWED_HOSTS_IP', default=False), env('ALLOWED_HOSTS_DOMAIN', default=False), 'localhost']


# Application definition

INSTALLED_APPS = [
    'ML_App.apps.MlAppConfig',
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
    'whitenoise.middleware.WhiteNoiseMiddleware', # Renderデプロイ用に追加
]

ROOT_URLCONF = 'ML_Project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/'templates'],
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

WSGI_APPLICATION = 'ML_Project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'multigledb',
        'USER': 'multigle',
        'PASSWORD': env('DATABASES_PASSWORD',default=False),
        'HOST': '10.0.2.10',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT=BASE_DIR/'staticfiles'
STATICFILES_DIRS=[str(BASE_DIR/'static')]


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


#開発環境であればlocal_settingsを上書き
try:
    from .local_settings import *
except ImportError:
    pass


#Renderデプロイ用
if RENDER_DEPLOY:
    ALLOWED_HOSTS = [env('ALLOWED_HOSTS_DOMAIN', default=False), 'localhost']
    default_dburl = "sqlite:///" + str(BASE_DIR / "db.sqlite3")
    STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
    DATABASES = {
        "default": config("DATABASE_URL", default=default_dburl, cast=dburl),
    }

    SUPERUSER_NAME = env("SUPERUSER_NAME", default=False)
    SUPERUSER_EMAIL = env("SUPERUSER_EMAIL", default=False)
    SUPERUSER_PASSWORD = env("SUPERUSER_PASSWORD", default=False)
    