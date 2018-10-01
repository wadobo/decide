ALLOWED_HOSTS = ["*"]

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

APIS = {
    'authentication': 'http://10.5.0.1:8000',
    'base': 'http://10.5.0.1:8000',
    'booth': 'http://10.5.0.1:8000',
    'census': 'http://10.5.0.1:8000',
    'mixnet': 'http://10.5.0.1:8000',
    'postproc': 'http://10.5.0.1:8000',
    'store': 'http://10.5.0.1:8000',
    'visualizer': 'http://10.5.0.1:8000',
    'voting': 'http://10.5.0.1:8000',
}

BASEURL = 'http://10.5.0.1:8000'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': '5432',
    }
}

# number of bits for the key, all auths should use the same number of bits
KEYBITS = 256
