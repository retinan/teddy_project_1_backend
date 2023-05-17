from .base import *

DEBUG = False

ALLOWED_HOSTS = ["*"]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'retinan$teddy_project_1',
        'USER': 'retinan',
        'PASSWORD': 'qwrt12@@',
        'HOST': 'retinan.mysql.pythonanywhere-services.com',
        'PORT': '3306',
    }
}
