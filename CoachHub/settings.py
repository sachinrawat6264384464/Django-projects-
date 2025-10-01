import os
import dj_database_url
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Secret Key
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "fallback-secret")

# DEBUG
DEBUG = os.getenv("DJANGO_DEBUG", "False") == "True"

# Allowed hosts
ALLOWED_HOSTS = ["books-room.onrender.com"]  # Render URL

# DATABASES: Supabase remote Postgres
DATABASES = {
    'default': dj_database_url.config(
        default=f"postgres://{os.getenv('DB_USER','postgres')}:" \
                f"{os.getenv('DB_PASSWORD','YOUR_PASSWORD')}@" \
                f"{os.getenv('DB_HOST','db.odbrncozvpukbshkwyvp.supabase.co')}:" \
                f"{os.getenv('DB_PORT','5432')}/" \
                f"{os.getenv('DB_NAME','postgres')}",
        conn_max_age=600,
        ssl_require=True  # SSL required for Supabase
    )
}

# Static files
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]  # Dev
STATIC_ROOT = BASE_DIR / "staticfiles"    # Production

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"

# Installed apps & middleware (same as before)
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

# Default primary key
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
