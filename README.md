levsdelight2
============

Django App using AngularJS, Grunt, Less, CoffeeScript

### To start the local development environment:

1. Install Postgressql (MACOSX Postgres.app)
2. Install the [Heroku Toolbelt](https://toolbelt.heroku.com/)
2. create database `createdb -h localhost levsdelight2`
3. create virtual fish environment `vf new levsdelight`
4. connect virtual env to directory `cd ~/Project/levsdelight2 && vf connect`
5. Install python dependencies `pip install Django psycopg2 gunicorn dj-database-url`
6. Build Django project here: `django-admin.py startproject levsdelight2 .`
7. Create new app for project: `python manage.py startapp levsdelight_com`
7. Make a new file called Procfile to start the web dyno for Heroku
`
echo "web: gunicorn levsdelight2.wsgi" > Procfile
`
8. Make sure it works `foreman start` then `Ctrl+C` to quit
9. Create the requirements.txt file for Heroku to install dependencies `pip freeze > requirements`
10. In settings.py:
 * uncomment admin in installed apps section
 * add levsdelight_com in installed apps section
 * add this code to the bottom of settings.py

```python
try:
  from local_settings.py import *
except ImportError:
  # Parse database configuration from $DATABASE_URL
  import dj_database_url
  DATABASES['default'] =  dj_database_url.config()

  # Honor the 'X-Forwarded-Proto' header for request.is_secure()
  SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
```

11. Create local_settings.py and add this code:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'levsdelight2',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '5432',                      # Set to empty string for default.
    }
}

```

### Build First table and populate it

1. Add this code to models.py

```python
from django.db import models

class Slideshow(models.Model):
    title = models.CharField(max_length=1000)
    desc = models.CharField(max_length=2000)
    pictureLocation = models.CharField(max_length=200)
    isActive = models.BooleanField()
    slideshow_id = models.IntegerField()
    order_id = models.IntegerField()
    pub_date = models.DateTimeField('date_pubished')

    def __unicode__(self):
        return "Title: \"%s\" for Slideshow: \"%s\"" % (self.title, str(self.slideshow_id))
```

2. So we can administer the Slideshow table through Django's admin section add slideshow to `levsdelight_com/admin.py`

```python
from django.contrib import admin
from levsdelight_com.models import Slideshow
admin.site.register(Slideshow)
```

3. Build the database: `python manage.py syncdb`


### Create the repo :)
1. `git init .`
2. `git add .`
3. `git commit -m 'my first commit`
4. Create the .gitignore file

```python
.venv
.*.pyc
local_settings.py
```

5. git push remote_name branch_name 

### Deploy app to Heroku

1. Login to Heroku
2. heroku create
3. git push heroku master
4. Sync the database `heroku run python manage.py syncdb`



