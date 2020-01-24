% prepara el repositorio para su despliegue.
release: sh -c 'cd decide && python3 manage.py migrate'
% especifica el comando para lanzar Decide
web: sh -c 'cd decide && gunicorn decide.wsgi --log-file -'
