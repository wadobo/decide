DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}

STATIC_ROOT = '/app/static/'
MEDIA_ROOT = '/app/static/media/'
ALLOWED_HOSTS = ['*']

# Modules in use, commented modules that you won't use
MODULES = [
    'authentication',
    'base',
    'booth',
    'census',
    'mixnet',
    'post_processed',
    'store',
    'visualizer',
    'voting',
]

APIS = {
    'authentication': 'http://localhost:8000/',
    'base': 'http://localhost:8000/',
    'booth': 'http://localhost:8000/',
    'census': 'http://localhost:8000/',
    'mixnet': 'http://localhost:8000/',
    'post_processed': 'http://localhost:8000/',
    'store': 'http://localhost:8000/',
    'visualizer': 'http://localhost:8000/',
    'voting': 'http://localhost:8000/',
}
