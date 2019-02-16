# cerebro

In one shell, run server:

```
$ make run
...
```

In another, load data, then connect:

```
$ make load
...
$ make connect
...
postgres=#
```

## Django-portion: 

Currently the Django portion of this project is in development and set to use SQLite. To set things up locally: 
    1. Ensure packages in `requirements.txt` are installed
    2. From the Django project root directory [cerebro](cerebro) run `python manage.py makemigrations; python manage.py migrate`
    3. Create a superuser with `python manage.py createsuperuser` and follow prompts (login is required to view data) 
    4. Populate your local SQLite database with fake data by running the `populate_fake_database.py` script
    5. Start up a local dev. server with `python manage.py runserver`; the default site root is [http://127.0.0.1](http://127.0.0.1)
    6. Navigate to [http://127.0.0.1/admin](http://127.0.0.1/admin) and login with your created superuser
    7. Navigate to [http://127.0.0.1/members](http://127.0.0.1/members) to see a list of (fake) AGAMembers


