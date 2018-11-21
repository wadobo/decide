release: sh -c 'cd decide && python manage.py migrate'
web: sh -c 'cd decide && gunicorn decide.wsgi --log-file -'
