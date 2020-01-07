#Base image
FROM python:3.6

# Create and set working directory
RUN mkdir /app
WORKDIR /app

# Add current directory code to working directory
RUN . /app
COPY gunicorn.conf /etc/supervisor/conf.d/
RUN mkdir -p /var/log/gunicorn

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
RUN supervisorctl update
COPY django.conf /etc/nginx/sites-available/
RUN ln /etc/nginx/sites-available/django.conf /etc/nginx/sites-enabled/
RUN nginx