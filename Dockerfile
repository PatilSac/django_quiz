FROM python:3.9.0a2-alpine3.10
RUN apt-get install -y git
RUN apt-get install -y python3-pip
RUN apt-get install -y nginx
RUN apt-get install -y supervisor
RUN git clone https://github.com/PatilSac/django_quiz.git
RUN pip3 install gunicorn
RUN pip3 install -r /home/ubuntu/django_quiz/requirement_file.txt
RUN mv /home/ubuntu/django_quiz/gunicorn.conf /etc/supervisor/conf.d/
RUN mkdir /var/log/gunicorn
RUN supervisorctl update
RUN mv /home/ubuntu/django_quiz/django.conf /etc/nginx/sites-available/
RUN ln django.conf /etc/nginx/sites-enabled/
RUN nginx

