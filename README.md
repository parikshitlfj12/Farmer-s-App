# Farmer-s-App
A farmer business website

# Web Application on the following Tech-Stack:
Django, PostGreSQL, HTML, CSS, JS, Bootstrap, JQuery.
API's include Twilio, Gmail, Paypal.

# Pre-requisite - 
Django. https://docs.djangoproject.com/en/3.0/topics/install/
PostgreSQL. https://www.postgresql.org/download/
To operate on API's create developer's account for all of them.
Twilio - https://www.twilio.com/try-twilio
Paypal - https://www.paypal.com/signin/client?flow=provisionUser&country.x=US&locale.x=en_US
Gmail - https://console.developers.google.com/

# Pre-running setup-
1. Before running the server make sure your database (PostgreSQL) is connected to your django application.
While installing postgreSQL software you might have set your username and password. Copy paste them in the project/settings.py file.
-> DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'databasename',
        'USER' : 'username',
        'PASSWORD' : 'password',
        'HOST' :'localhost'
      }
  }
  
2.  Creating database tables, migrating models.
    Run the following command.
    -> python manage.py makemigrations
    -> python manage.py migrate
    To cross check the successfull migrations go to your database GUI and check for tables. You'll see new tables popping up.
   
3. Serve Static Files.
    In project/settings.py make sure you have the code as follows.
    ->STATIC_URL = '/static/'
      STATICFILES_DIRS = [
          os.path.join(BASE_DIR, 'static')
      ]
      STATIC_ROOT = os.path.join(BASE_DIR, 'assets')
     Now run the command-
     ->python manage.py collectstatic
     
 # Running the Server
 Now that we are all set up with the project it's time to run it.
 -> python manage.py runserve
 Go to your browser and type localhost:8080
 Here comes your Happy Farm's Webapp

   
