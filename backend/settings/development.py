from .base import *

DEBUG = True

ALLOWED_HOSTS = ["*"]


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'akynmyot',
#         'USER': 'akynmyot',
#         'PASSWORD': '1RZnjual1iA42eFM8CVRKuwxpTz8hswM',
#         'HOST': 'arjuna.db.elephantsql.com',
#         'PORT': '5432',
#     }
# }

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
