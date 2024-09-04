import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

ALLOWED_HOSTS = [os.getenv('ALL_HOST1'), os.getenv('ALL_HOST2')]
INTERNAL_IPS = None

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASS'),
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
