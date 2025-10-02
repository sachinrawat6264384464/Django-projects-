import os
from pathlib import Path
import dj_database_url
CSRF_TRUSTED_ORIGINS = ["https://web-production-50fc0.up.railway.app"]

# =========================
# Base directory
# =========================
BASE_DIR = Path(__file__).resolve().parent.parent

# =========================
# Security
# =========================
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "changeme-secret-key")
DJANGO_DEBUG= True

# Allowed Hosts
ALLOWED_HOSTS = ["*"]
# =========================
# Database (Railway PostgreSQL)

# CSRF Trusted Origins (Railway ke liye zaroori)
CSRF_TRUSTED_ORIGINS = [
    'https://web-production-50fc0.up.railway.app'  # tumhara Railway web app URL
]
# =========================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'railway',  # Railway DB ka name
        'USER': 'postgres', # Railway DB ka user
        'PASSWORD': 'NJmNqYrfkSQnoNEPIREPerAMznnEKWIf',  # Railway DB password
        'HOST': 'interchange.proxy.rlwy.net',  # Railway DB host
        'PORT': '37784',  # Railway DB port
    }
}


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
    'EduTrack',
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
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # add this
    'django.contrib.sessions.middleware.SessionMiddleware',
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
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
# Password validation
# =========================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
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
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]  # tumhara local static folder
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')   # collectstatic ke liye

# =========================
# Default primary key
# =========================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
