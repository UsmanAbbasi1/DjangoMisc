# use image 'python:3.8' for this container
FROM python:3.8
# set env var
ENV PYTHONUNBUFFERED 1
# run command to create directory named 'code' in container
RUN mkdir /code
# The WORKDIR instruction sets the working directory for any RUN, CMD, ENTRYPOINT, COPY and ADD instructions that follow it in the Dockerfile
WORKDIR /code
# copy 'reqs/requirements.txt' from project directory into container's ''/code/reqs/' directory
COPY reqs/requirements.txt /code/reqs/
# Again run command to install requirements in container
RUN pip install -r reqs/requirements.txt
# Cope application code into container's 'code' directory
COPY . /code/