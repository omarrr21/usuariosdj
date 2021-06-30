from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME':get_secret("DB_NAME"),
        'USER':get_secret("USER"),
        'PASSWORD':get_secret("PASSWORD"),
        'HOST':'localhost',
        'PORT':'5432',
    }
}


STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'static'),
)
MEDIA_URL = '/media/'
MEDIA_ROOT= os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'media')