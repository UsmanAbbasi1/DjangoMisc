# DjangoMisc

This project contains examples for following topics:
* JWT Authentication
* Setup Celery and Redis
* Caching in Django
* Management Commands
* Set up static files in Django
* Setup docker (Will add later)

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
