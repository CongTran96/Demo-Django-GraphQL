# Demo-Django-GraphQL

## Example use GraphQL with django

Sorry, I'm a bad english.

First, Open cmd with **admin option** and type following.

1. Install python

go to [python installer](https://www.python.org/downloads/release/python-365/) then download and install. Make sure check `add Python to Path` while install python.

Make sure you install python's version <= 3.6. Python 3.7 has problem when interact with django.

2. Install Virtualenv

make sure you has been installed pip before.

``` pip install virtualenv ```

3. Make Virtual Enviroment and active this

``` python -m venv myvenv ```

Virtual Enviroment with name `myvenv`. Check by type ` dir`


Active virtualenv

``` myvenv\Scripts\activate ```

4. Upgrade pip and Install django

Update your pip

``` python -m pip install --upgrade pip ```

Just install django framework in your computer.
Use django version 1.11.0 for stable and more communication.

``` pip install django~=1.11.0 ```

5. Go to project, migrate database and make admin user

Go to project.

``` cd graphql_demo ```

Migrate database with.

``` python manage.py makemigration```

Sync database into sqllite3.

``` python manage.py migrate ```

create super user.

``` python manage.py createsuperuser ```

type account, email, password what ever you want.


6. Install django-graphene for GraphQL

Run ``` pip install graphene-django ```

7. Install django filter for GraphQL

Run ``` pip install django-filter ```





