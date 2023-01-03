Boilerplate apps
================

### What is this?
Django boilerplate apps are a collection of apps that can be used to quickly.
get started with a new Django project. They are designed to be used as a base for a new project.
They are not designed to be used as a standalone app.

### Why?
I have found that I often start a new project with the same basic setup. I have a base project that I use as a starting point. I then copy the apps I need from that project into the new project. This is a pain and I wanted to make it easier.

### Setup instructions
1. Clone the repo
    ```shell
    git clone ...
   
   cd boilerplate
    ```
2. Run in Docker ([see below](#setup-django-boilerplate-with-docker))
3. Run in Local ([see below](#setup-django-boilerplate-with-local))

#### Setup Django Boilerplate with Docker
- Build and run the docker container
    ```shell
    docker-compose up -d --build
    ```
- Run the migrations
    ```shell
    docker-compose exec web python manage.py migrate
    ```
- Create a superuser
    ```shell
    docker-compose exec web python manage.py createsuperuser
    ```
- Run the tests
    ```shell
    docker-compose exec web python manage.py test
    ```
- Run the server
    ```shell
    docker-compose exec web python manage.py runserver
    ```


#### Setup Django Boilerplate with Local
- Create a virtual environment
    ```shell
    python3 -m venv venv
    ```
- Activate the virtual environment
    ```shell
    source venv/bin/activate
    ```
- Install the requirements
    ```shell
    pip install -r requirements.txt
    ```
- Setup Environment Variables and change values as needed
    ```shell
    cp .env.example .env
    ```
- Run the migrations
    ```shell
    python manage.py migrate
    ```
- Create a superuser
    ```shell
    python manage.py createsuperuser
    ```
- Run the tests
    ```shell
    python manage.py test
    ```
- Run the server
    ```shell
    python manage.py runserver
    ```
  