# My-Diary

### This Project for Tinkerhub Co-coder event

![preview](previews/preview.png)

## Team members

1. <a href="https://github.com/amjadcp/">Amjad C P</a>
2. <a href="https://github.com/Abbie2002/">Abbie Thankachan</a>

## Team Id

Python/210

## Link to product walkthrough

<a href="https://www.loom.com/share/befdc5eb98df442884e4cd23c5e4eeb2?sharedAppSource=personal_library"><strong>Click »</strong></a>

[![TASK-CLI](previews/preview.png)](https://www.loom.com/share/befdc5eb98df442884e4cd23c5e4eeb2?sharedAppSource=personal_library)

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/amjadcp/diary-app.git
$ cd diary-app
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ python -m venv env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(E-shelf)$ pip install -r requirements.txt
```

Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:

create databse using

```sh
$ python manage.py migrate
```

Then run the server using

```sh
$ python manage.py runserver
```

And navigate to `http://127.0.0.1:8000/`.

## Libraries used

1. asgiref==3.5.0
2. backports.zoneinfo==0.2.1
3. dj-database-url==0.5.0
4. Django==4.0.2
5. django-heroku==0.3.1
6. gunicorn==20.1.0
7. importlib-metadata==4.11.2
8. Markdown==3.3.6
9. psycopg2==2.9.3
10. sqlparse==0.4.2
11. whitenoise==6.0.0
12. zipp==3.7.0
