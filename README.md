# DjangoMisc

This project will contain examples for following topics:
* Caching in Django
* Setup celery
* Management Commands
* Setup docker
* Set up static files in Django
* Signals

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

