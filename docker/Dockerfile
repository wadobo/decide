from python:alpine

RUN apk add --no-cache git postgresql-dev gcc libc-dev

RUN pip install gunicorn
RUN pip install psycopg2
RUN pip install ipdb
RUN pip install ipython

WORKDIR /app

RUN git clone https://github.com/wadobo/votinus.git .
RUN pip install -r requirements.txt

WORKDIR /app/votinus

# local settings.py
ADD docker-settings.py /app/votinus/local_settings.py

RUN ./manage.py collectstatic

#CMD ["gunicorn", "-w 5", "votinus.wsgi", "--timeout=500", "-b 0.0.0.0:5000"]
