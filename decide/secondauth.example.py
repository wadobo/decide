from decide.settings import *

# Modules in use, commented modules that you won't use
MODULES = [
    'mixnet',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db2.sqlite3'),
    }
}

BASEURL = 'http://localhost:9000'
