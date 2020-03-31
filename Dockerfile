# use image 'python:3.8' for this container
FROM python:3.8

# set env var
ENV PYTHONUNBUFFERED 1

# run command to create directory named 'code' in container
RUN mkdir /code

# The WORKDIR instruction sets the working directory for any RUN, CMD, ENTRYPOINT, COPY and ADD instructions that follow it in the Dockerfile
WORKDIR /code

# Copy application code into container's 'code' directory
COPY . /code/

# Run command to install requirements in container
RUN pip install -r ./reqs/requirements.txt
