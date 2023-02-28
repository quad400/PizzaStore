import os

from dotenv import load_dotenv
from pathlib import Path

load_dotenv()


BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-#!u8&1bee6d@d1m#%#3pb-+(el%56o%czwl(8y^@pfbn1(s03('

DEBUG = True

ALLOWED_HOSTS = []


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Third Party
    'mptt',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # app
    'pizza'

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

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/ 'templates'],
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

WSGI_APPLICATION = 'core.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': str(os.getenv("DB_NAME")),
        'USER': str(os.getenv("DB_USER")),
        'PASSWORD': str(os.getenv("DB_PASSWORD")),
        'HOST':str(os.getenv("DB_HOST")),
        'PORT': str(os.getenv("DB_PORT")),
    }
}


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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True



STATIC_URL = 'static/'
STATIC_ROOT = 'static_root'
STATICFILES_DIRS = [BASE_DIR / 'static']

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend'
)

# ...
SITE_ID = 1
ACCOUNT_EMAIL_REQUIRED=True
# ACCOUNT_EMAIL_VERIFICATION='mandatory'
LOGIN_REDIRECT_URL='/'
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

STRIPE_PUBLISHABLE_KEY = str(os.getenv("STRIPE_PUBLISHABLE_KEY"))
STRIPE_SECRET_KEY = str(os.getenv("STRIPE_SECRET_KEY"))
STRIPE_WEBHOOK_KEY = str(os.getenv("STRIPE_WEBHOOK_KEY"))