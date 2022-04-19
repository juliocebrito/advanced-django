# Advance Django
For Educational Purposes Only

## dependecies
* python 3
* sqlite
* postgres (optional)
* docker (optional)

---

## Setup
* git clone https://github.com/juliocebrito/advanced-django
* cd advance_django
* mkdir templates static media temp
* python3 -m venv .venv
* source .venv/bin/activate
* pip install -r requirements_local.txt
* python manage.py migrate
* python manage.py createsuperuser
* pytthon manage.py runserver

---

# Apps
## Polls
## Books
## Blog
## Users

---

# Subjects:
## Django Architecture

## MTV VS MVC

## Django Request-Response Cycle 

## Request and response objects
https://docs.djangoproject.com/en/4.0/ref/request-response/

## settings

## requirements

## libs

---

# Advanced Models
https://docs.djangoproject.com/en/4.0/topics/db/models/

## Fields
* blank
* null
* help_text

## Ralationships
* Many-to-one relationships
* Many-to-many relationships
* Extra fields on many-to-many relationships
* One-to-one relationships

## Validators
https://docs.djangoproject.com/en/4.0/ref/validators/

## Meta
* abstrac
* proxy

## Migrations
https://docs.djangoproject.com/en/4.0/topics/migrations/

* python manage.py makemigrations
* python manage.py makemigrations app
* python manage.py makemigrations app 0000
* python manage.py makemigrations --name foo app
* python manage.py makemigrations --empty app
* python manage.py migrate
* python manage.py migrate app
* python manage.py migrate app 0000
* python manage.py showmigrations
* python manage.py sqlmigrate app 0000

## ORM (Object-relational mapper)
https://docs.djangoproject.com/en/4.0/topics/db/queries/

---

# Advance Views
* Class-based views
https://docs.djangoproject.com/en/4.0/ref/class-based-views/
https://ccbv.co.uk/

---

# Advance Templates

---

# Advanced Forms
* forms
https://docs.djangoproject.com/en/4.0/topics/forms/
https://docs.djangoproject.com/en/4.0/ref/forms/api/

* Formsets
https://docs.djangoproject.com/en/4.0/topics/forms/formsets/

---

# Advanced URLs
https://docs.djangoproject.com/en/4.0/topics/http/urls/

# Advance Admin
* Actions

---

# Auth
* users
https://docs.djangoproject.com/en/4.0/topics/auth/default/#using-the-views-1

---

# Common web application tools
* Caching
* Logging
* Sending emails
* Syndication feeds (RSS/Atom)
* Pagination
* Messages framework
* Serialization
* Sessions
* Sitemaps
* Static files management
* Data validation

---

# Other core functionalities
* Conditional content processing
* Content types and generic relations
* Flatpages
* Redirects
* Signals
* System check framework
* The sites framework
* Unicode in Django