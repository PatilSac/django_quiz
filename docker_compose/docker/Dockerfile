FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN apt-get install -y supervisor
RUN mkdir /code
WORKDIR /code
COPY requirement_file.txt /code/
COPY gunicorn.conf /etc/supervisor/conf.d/
RUN pip3 install -r requirement_file.txt
RUN mkdir -p /var/log/gunicorn
RUN supervisorctl update
COPY django.conf /etc/nginx/sites-available/
RUN ln /etc/nginx/sites-available/django.conf /etc/nginx/sites-enabled/
RUN nginx

COPY . /code/
