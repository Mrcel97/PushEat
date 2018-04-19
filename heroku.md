### Heroku deployment

First, you must ensure that the requirements.txt file is right, you will need, at least: pycopg2, dj-database-url, and gunicorn (besides Django, obviously).

So you check your requirements.txt to have at least:

    Django==1.11.10
    psycopg2==2.7.3.1
    dj-database-url
    gunicorn

Then, you add a new file on the project root (where manage.py resides), called Procfile (careful with capitals), with:

    web: gunicorn PushEatApp.wsgi --log-file -

This will tell heroku how to run your program, in this case, by using gunicorn with the wsgi package inside your project directory (PushEatApp). And to send all logs to standard output ("-"), so heroku can capture it.

We also add a file to tell Heroku that your project is a python one, and to tell it which python version to use, in our case, to be coherent with the labs and with docker deployment, 2.7.14. The file should be called runtime.txt and it will must contain:

    python-2.7.14

Afterward, assuming you already have a repository git created put in terminal:

    git add *
    git commit -m "Init heroku"

After that, we can create a heroku application with the command:

    heroku create

That will add a new git remote repository, you can check with:

    git remote -v
    
You can deploy to heroku, then, with:

    git push heroku master
    
If the last command fails or imports pyhton 3 instead of python 2.7 that is specified into the runtime.txt. You have to introduce the following command:
    
    heroku stack:set cedar-14 -a <app_name>
    
You can run into an error concerning static files, you will fix it correctly later, for now, we can "skip" the error with:

    heroku config:set DISABLE_COLLECTSTATIC=1

You can then connect, if all goes ok to your app with:

    heroku open

If you run into errors with hosts not in ALLOWED_HOSTS, you can fix it by editing settings.py, and adding the suggested host in the error page to ALLOWED_HOSTS variable.

    ALLOWED_HOSTS = ['PushEat.herokuapp.com']
    
Furthermore, you have to introduce the following commands:

    git add PushEatApp/settings.py
    git commit -m "Fixed"
    git push heroku master

If the connection is ok you'll probably get an error related to missing tables. You should correct it as you'd do when locally developing with django, but running the migrations in heroku not locally:

    heroku run python manage.py migrate
    heroku run python manage.py createsuperuser
    heroku open
    
 ### Static files the right way

Then, you must add to MIDDLEWARE on settings.py:

    'whitenoise.middleware.WhiteNoiseMiddleware',
    
On the STATIC_URL on settings.py substitute it by:

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/1.11/howto/static-files/

    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

    STATIC_URL = '/static/'
    # Extra places for collectstatic to find static files.
    STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    )
    STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

And to requirements.txt add:

    whitenoise

Finally, you have to send the files to heroku again:

    git add PushEatApp/settings.py
    git add requirements.txt
    git commit -m "Added whitenoise"
    git push heroku master


    
