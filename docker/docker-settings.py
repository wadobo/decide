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
    'postproc',
    'store',
    'visualizer',
    'voting',
]

BASEURL = 'http://localhost:5000'

APIS = {
    'authentication': 'http://localhost:5000',
    'base': 'http://localhost:5000',
    'booth': 'http://localhost:5000',
    'census': 'http://localhost:5000',
    'mixnet': 'http://localhost:5000',
    'postproc': 'http://localhost:5000',
    'store': 'http://localhost:5000',
    'visualizer': 'http://localhost:5000',
    'voting': 'http://localhost:5000',
}
