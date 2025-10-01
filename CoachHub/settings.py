from pathlib import Path
import os
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

# Secret Key
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "fallback-secret")

# Production pe DEBUG = False
DEBUG = False  

ALLOWED_HOSTS = ["*"]  # sab hosts allow karega


# Installed Apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'EduTrack',
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

ROOT_URLCONF = 'CoachHub.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
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

import dj_database_url
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get("DATABASE_URL"),  # must come from environment variable
        conn_max_age=600,
        ssl_require=True
    )
}



# Static files
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]   # dev ke liye
STATIC_ROOT = BASE_DIR / "staticfiles"     # production ke liye collectstatic

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"           # uploaded videos/images ke liye


# Default PK
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
