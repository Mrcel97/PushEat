#Docker deployment instructions

#####Dockerfile
Once requirements.txt is OK, we'll create the Dockerfile for our django application container.

Create a file called: Dockerfile (Case-Sensitive) with:

    FROM python:2.7.14
    RUN mkdir /app
    WORKDIR /app
    ADD requirements.txt /app/
    RUN pip install -r requirements.txt
    ADD . /app/

This file states:

    Inherit from python container, with python 2.7.14.
    Create a directory inside our container, called /app .
    Start working inside that directory.
    Copy requirements.txt file from our working directory on the host to /app on the container.
    Install everything mandated by requirements.txt.
    Copy the rest of the project to /app

Then we can test that it builds correctly:
    
    docker build .

(The dot at the end means: on the current directory, and will search for a Dockerfile file.)

If it builds OK we can go to the next step, otherwise, we solve the building errors.

#####Orchestrate with docker-compose
    
To create an orchestration, that is, a set of different containers that will compose our application, 
we first create a file named docker-compose.yml on current (application) dir:

    version: "2.0"
    services:
      db:
        image: postgres
      web:
        build: .
        command: python manage.py runserver 0.0.0.0:8000
        volumes:
          - .:/app
        ports:
          - "8000:8000"
        depends_on:
          - db

Take into account that this file is in YAML format, so spaces and tabs mean something. If possible use an editor que 'understands' YAML

Once you have this compose file, you can build it with:

docker-compose build

And, when built, we can start the orchestration with:

    docker-compose up

If everything works, we'll have, on screen, the logs of both containers that comprise the orchestration, namely, a postgres db, and a django container (built with the Dockerfile we wrote above).

If, due to delays in the initial startup of the database container (postgres in its first run initializes the database, and that process can take a bit to run), django container fails due to not being able to connect to the database, just stop docker-compose (CRTL+C), and restart it, the next time, the database will boot up faster.

When running, we can connect to the django web server, on:

    http://127.0.0.1:8000/

If we receive an error referring to the ALLOWED_HOSTS variable, we can edit the settings.py file, locate the ALLOWED_HOSTS variable, adding the values that Django mentions on the error page, and then rebuild the containers and boot them again:

    docker-compose build
    docker-compose up

If we then try to connect again, we'll receive an error page mentioning that some database tables do not exist, we should run then the migrate and the createsuperuser commands. But for it to work, we should run it inside the Django container with:

    docker-compose run web python manage.py migrate
    docker-compose run web python manage.py createsuperuser
