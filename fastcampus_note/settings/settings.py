"""
Django settings for fastcampus_note project.

Generated by 'django-admin startproject' using Django 3.2.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
import platform
from pathlib import Path
from platform import system as sys

from dotenv import load_dotenv, dotenv_values

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-nuad^31yi$l(goh+kw$u4mjq=na_jcmtg+oh5ohs!$btph7lu2"

# dev, prd, test
ENV = os.getenv("DJANGO_ENV", "dev")
LOCAL = True if sys().lower().startswith("darwin") or sys().lower().startswith("windows") else False

# SECURITY WARNING: don't run with debug turned on in production!
if ENV == "prd":
    DEBUG = True
else:
    DEBUG = False

if ENV == "prd":
    ALLOWED_HOSTS = ["abc@gmail.com"]
else:
    ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "app",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "fastcampus_note.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "app.context_processor.renderer",
            ],
        },
    },
]

WSGI_APPLICATION = "fastcampus_note.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
ENV_LOC = BASE_DIR / "fastcampus_note/settings/.env"
ENV_LOAD = load_dotenv(ENV_LOC)

if ENV_LOAD:
    config = dotenv_values(ENV_LOC)
    DB_HOST = config.get("DB_HOST")
    DB_USER = config.get("DB_USER")
    DB_PASS = config.get("DB_PASS")
else:
    DB_HOST = os.environ.get("DB_HOST")
    DB_USER = os.environ.get("DB_USER")
    DB_PASS = os.environ.get("DB_PASS")

DATABASES = {
    "default": {
        "NAME": "note_hub",
        "ENGINE": "django.db.backends.mysql",
        "USER": DB_USER,
        "PASSWORD": DB_PASS,
        "HOST": DB_HOST,
        "PORT": "3306",
        "OPTIONS": {
            "autocommit": True,
            "charset": "utf8mb4",
        },
    }
}

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        "OPTIONS": {
            "min_length": 9,
        },
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
if DEBUG:
    LOGIN_URL = "/login"
else:
    LOGIN_URL = "/production/login"


CACHES = {
    # python manage.py createcachetable
    "default": {
        "BACKEND": "django.core.cache.backends.db.DatabaseCache",
        "LOCATION": "cache_table",
    }
}

# Local Memory
# CACHES = {
#     "default": {
#         "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
#     }
# }

# Redis
# CACHES = {
#     "default": {
#         "BACKEND": "django_redis.cache.RedisCache",
#         "LOCATION": "redis://127.0.0.1:6379/1",  # 1번 DB
#         "OPTIONS": {"CLIENT_CLASS": "django_redis.client.DefaultClient"},
#     },
# }


# File-based cache
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
#         'LOCATION': BASE_DIR / 'django_cache',
#     }
# }

""" ADDITIONAL CONFIG """
# ADMINS = [("ryan", "ryan@abc.com")]  # https://docs.djangoproject.com/en/4.1/ref/logging/#django.utils.log.AdminEmailHandler
# APPEND_SLASH = True  # CommonMiddleware
# PREPEND_WWW = True  # CommonMiddleware
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
#     }
# }

# DEFAULT_FROM_EMAIL = "ryan@abc.com"
# https://docs.djangoproject.com/en/4.1/ref/settings/
