import os
from pathlib import Path
import environ
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
environ.Env.read_env()

SECRET_KEY = env('SECRET_KEY') 

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1','baba-voss.herokuapp.com','www.babavoss.site']


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "whitenoise.runserver_nostatic",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "bootstrap5",
    "resturant",
    "rest_framework",
    "rest_framework.authtoken",
    "dj_rest_auth",
    "django.contrib.sites",
    "dj_rest_auth.registration",
    "storages",
    
]

PAYPAL_CLIENT_ID  = env('PAYPAL_CLIENT_ID')
PAYPAL_SECRET_ID  = env('PAYPAL_SECRET_KEY')
PAYPAL_MODE       = env('PAYPAL_MODE')

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': ['rest_framework.authentication.TokenAuthentication']
}

SITE_ID = 1

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ['templates'],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "project.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }
import dj_database_url
DATABASES_URL = env('DATABASE_URI')


DATABASES = {
   'default': {
       'ENGINE'  : env('DATABASE_ENGINE'),
       'NAME'    : env('DATABASE_NAME'),
       'USER'    : env('DATABASE_USER'),
       'PASSWORD': env('DATABASE_PASS'), 
       'HOST'    : env('DATABASE_HOST') ,      
       'PORT'    : env('DATABASE_PORT') ,      
       'URI'     : env('DATABASE_URI') ,      
   }
}

EMAIL_BACKEND       = env('EMAIL_BACKEND')
EMAIL_HOST          = env('EMAIL_HOST')
EMAIL_USE_TLS       = env('EMAIL_USE_TLS')
EMAIL_PORT          = env('EMAIL_PORT')
EMAIL_HOST_USER     = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

USE_I18N = True
USE_L10N = False
USE_TZ = False

LANGUAGE = (('ar','Arabic'),('en','English'),)

LOCALE_PATHS = (os.path.join(BASE_DIR, 'locale/'),)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')
STATICFILES_DIRS = (os.path.join(BASE_DIR,'static'),)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
MEDIA_DIRS = (os.path.join(BASE_DIR,'mediafiles'),)

AWS_ACCESS_KEY_ID ='AKIASDM5QDFBL2BKJ27N'
AWS_SECRET_ACCESS_KEY ='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'
AWS_STORAGE_BUCKET_NAME ='baba-voss23'
AWS_S3_SIGNATURE_NAME ='s3v4' 
AWS_S3_REGION_NAME ='us-east-1'
AWS_S3_FILE_OVERWRITE =False 
AWS_DEFAULT_ACL =None
AWS_S3_VERITY =True
DEFAULT_FILE_STORAGE ='storages.backends.s3boto3.S3Boto3Storage'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field
if os.getcwd() == '/resturant':
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_SSL_REDIRECT = True
    DEBUG = False
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
