"""
Django settings for pwfbackend project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'k$3@jk+61=2eu8*7f*@vhxuy(d_33ltu3i467__l!vjjdn7b4t'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'corsheaders',
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app.index',
    'app.categories',
    'app.recipes',
    'app.blog',
    'app.visits',
    'app.config',
    'ckeditor',
    'django_user_agents',
    
]

CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_user_agents.middleware.UserAgentMiddleware',
]

ROOT_URLCONF = 'pwfbackend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates/'), ],
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

WSGI_APPLICATION = 'pwfbackend.wsgi.application'
USER_AGENTS_CACHE = None

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB','pwfood'),
        'USER': os.getenv('POSTGRES_USER','pwfood'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD','abc123'),
        'HOST': os.getenv('POSTGRES_HOST','pwf-db') ,
        'PORT': os.getenv('POSTGRES_PORT', 5432),
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

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Managua'

USE_I18N = True

USE_L10N = False

USE_TZ = True

LOCALE_PATHS = (
 os.path.join(BASE_DIR, "locale"),
)



CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static2/"),
)

#media config
MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

GEOIP_PATH = os.path.join(BASE_DIR, 'geoip/')

SITE_URL = 'https://www.playingwithfoodni.com'

# jazzmin settings

JAZZMIN_SETTINGS = {
    'site_title' : 'PWF Panel de Administración',
    'site_header' : 'PWF',
    "custom_links": {
        "visits": [{
            "name": "Reportes",
            "url": "/reports",
            "icon": "fas fa-comments",
        }]
    },
    "show_ui_builder": True,
    "theme": "simplex",
}

JAZZMIN_UI_TWEAKS = {
    "theme": "simplex",
    "dark_mode_theme": "darkly",
}

JAZZMIN_SETTINGS["show_ui_builder"] = True

MAILJET_APIKEY = os.getenv('MAILJET_APIKEY','')
MAILJET_APISECRET = os.getenv('MAILJET_APISECRET','')


IP_DATA_APIKEY = '4563fe65e974231b53d1ff935b085f9dbbd8e17a939487edd05e1c36'

EMAIL_HOST = 'www.playingwithfoodni.com'
DEFAULT_FROM_EMAIL = 'automail@playingwithfoodni.com'#.format(socket.gethostname())
EMAIL_PORT = 25
EMAIL_USE_TLS = False

