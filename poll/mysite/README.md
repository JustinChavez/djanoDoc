# djanoDoc

Getting started

```
virtualenv .env

source .env/bin/activate

pip install django
```

Directory for HackerPack Dashboard

```
cd poll/mysite
```

Runserver

```
python manage.py runserver
```
<h1>PostgreSql</h1>
<h3>Starting Guide, may not be all correct</h3>
First, to install it postgresql, have homebrew install and thenn
```
brew install postgresql
```
and then you can start the servers from brew, i don't know if you need to keep the servers on or what they do
```
brew services start postgresql
```
you can stop the services by
```
brew services start postgresql
```
when you start the services you won't be able to do anything else i think so do 
```
cmd-t
```
to make a new window in the terminal, make sure to activate virtualenv also again
now guide is being taken from djangogirls guide by by Geek Girls Carrots and django-marcador tutorial licensed under Creative Commons Attribution-ShareAlike 4.0 International License

to create user enter in 
```
psql
```
to start the console of postgresql
now to create a user enter in
```
CREATE USER name;
```
and change name to what the name you want to be
then do
```
CREATE DATABASE djangogirls OWNER name;
```
and change name to the name you selected above and you can change djangogirls to what the name of the database you want to name it be
after that do 
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'djangogirls',
        'USER': 'name',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```
in settings.py where database is 
change NAME and USER to what you change it to be
make sure you are in virtualenv and do
```
pip install psycopg2
```
if you havent done it before
if you run
```
python -c "import psycopg2"
```
and it gives you no errors than you are good
now apply the migrate
```
python manage.py migrate
```
and then create a user
```
python manage.py createsuperuser --username name
```
replace name witha  user name you want





