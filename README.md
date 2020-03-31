# DjangoMisc

This project contains examples for following topics:
* Docker and DockerCompose. This app is containerized with different containers for django app, postgres, redis and celery.
* JWT Authentication
* Celery and Redis
* Caching in Django
* Management Commands
* Set up static files in Django

# Setup Redis:
* wget http://download.redis.io/redis-stable.tar.gz (Download)
* tar xvzf redis-stable.tar.gz (unzip)
* cd redis-stable
* make
* redis-server (run redis server)

# Setup Celery:
* Documentation link: http://docs.celeryproject.org/en/latest/getting-started/brokers/redis.html
* Install Celery and dependencies: pip install -U celery[redis]
* Run command for help: celery worker --help
* See django_misc/celery.py file for configurations.
* To run celery worker: celery worker -A django_misc --loglevel=INFO //django_misc is name of app where celery.py exists.

# Setup JWT Authentication
* Comments are added in code.
* Use this link for further guidance: https://getblimp.github.io/django-rest-framework-jwt/

# HOW TO RUN PROJECT:

Run following command in terminal to start project:

Steps:

1: Create Virtual environment:
* pip install virtualenv # Install 'virtualenv' package to create virtual environments
* virtualenv myenv -p python3 # Create virtual env with python 3
* source bin/activate. # start virtual env

2: Run postgres server:
* initdb pgsql/data (Only first time)
* pg_ctl -D pgsql/data -l logfile start (run serever everytime)

3: Run redis server:
* redis-server

4: Run celery worker:
* celery worker -A django_misc --loglevel=INFO //django_misc is name of app where celery.py exists.

4: Run Django server:
* python manage.py runserver
