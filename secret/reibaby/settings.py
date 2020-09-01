import os


# DEBUG
DEBUG = True

# Datebase for Django
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'reibabydb',
        'USER': 'admin',
        'PASSWORD': '20180105',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
