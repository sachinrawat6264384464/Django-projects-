import os
from pathlib import Path
import dj_database_url

# =========================
# Base directory
# =========================
BASE_DIR = Path(__file__).resolve().parent.parent

# =========================
# Security
# =========================
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "c2e6e1c108011290a3566bf7854d63bd")
DEBUG = os.getenv("DJANGO_DEBUG", "True") == "True"
# CoachHub/settings.py



ALLOWED_HOSTS = ["*"]


# =========================
# Installed apps
# =========================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'EduTrack',  # tumhara app
]

# =========================
# Middleware
# =========================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# =========================
# URLs & WSGI
# =========================
ROOT_URLCONF = 'CoachHub.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
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

WSGI_APPLICATION = 'CoachHub.wsgi.application'

# =========================
# Database (Supabase Postgres)
# =========================

import dj_database_url
import os

DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv("DATABASE_URL"),
        conn_max_age=600,
        ssl_require=True
    )
}

# =========================
# Password validation
# =========================
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

# =========================
# Internationalization
# =========================
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# =========================
# Static & Media files
# =========================
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]       # dev
STATIC_ROOT = BASE_DIR / "staticfiles"        # production

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"

# =========================
# Default primary key
# =========================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
