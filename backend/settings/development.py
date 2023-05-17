from .base import *

DEBUG = True

ALLOWED_HOSTS = ["*"]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'akynmyot',
        'USER': 'akynmyot',
        'PASSWORD': '1RZnjual1iA42eFM8CVRKuwxpTz8hswM',
        'HOST': 'arjuna.db.elephantsql.com',
        'PORT': '5432',
    }
}