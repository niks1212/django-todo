import os
from pathlib import Path

# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Secret key (you should set an environment variable for production)
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'your-secret-key')

# Determine if in development or production mode
DEBUG = os.getenv('DJANGO_DEBUG', '1') == '1'

# Allowed hosts for both development and production
ALLOWED_HOSTS = ['54.224.122.235', 'localhost', '127.0.0.1']
if not DEBUG:
    ALLOWED_HOSTS = ['*']

# Installed apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',  # Your To-Do application
    # Additional apps for development
    'django_extensions',  # Optional: for `runserver_plus` with HTTPS support
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URL configuration
ROOT_URLCONF = 'django_todo.urls'

# Templates configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'app/templates'],
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

# WSGI application
WSGI_APPLICATION = 'django_todo.wsgi.application'

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB', 'tododb'),
        'USER': os.getenv('POSTGRES_USER', 'user'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', 'password'),
        'HOST': 'db',
        'PORT': '5432',
    }
}

# Password validators
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Localization settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = '/app/static/'


# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# HTTPS and Security settings for production
if not DEBUG:
    SECURE_SSL_REDIRECT = True
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True
    SECURE_HSTS_SECONDS = 3600  # One hour; increase in production
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True

# Cross-Origin-Opener-Policy (COOP) header
SECURE_CROSS_ORIGIN_OPENER_POLICY = 'same-origin'

# Local HTTPS settings for development
if DEBUG and os.getenv('DJANGO_DEVELOPMENT') == '1':
    # Allow development HTTPS using runserver_plus with self-signed certs
    SECURE_SSL_REDIRECT = True
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True

