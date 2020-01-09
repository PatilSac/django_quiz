#Base image
FROM python:3.6
#copy content of the application to docker container app directory
COPY ./app /app

#change working dir to app
WORKDIR /app

# RUN mkdir -p /var/log/gunicorn
# RUN mkdir -p /etc/supervisor/conf.d/
# RUN pwd
# COPY /venv/quiz/gunicorn.conf /etc/supervisor/conf.d/
# RUN chmod +x /entrypoint.sh


# set defaut environment variables
ENV PYTHONUNBUFFERED 1


RUN apt-get update && apt-get install -y --no-install-recommends \
        python3-setuptools \
        python3-pip \
        python3-venv \
        supervisor \
        git \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# setup environment dependencies
RUN pip3 install -r requirement_file.txt

EXPOSE 8000

CMD ["gunicorn", "tickets.wsgi", "-b 0.0.0.0:8000"]



# RUN supervisorctl update
# COPY django.conf /etc/nginx/sites-available/
# RUN ln /etc/nginx/sites-available/django.conf /etc/nginx/sites-enabled/
# RUN nginx
