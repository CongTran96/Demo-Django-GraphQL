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

4. Install some library needed

``` pip install -r requirements.txt ```

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


6. Run server and make some example data for Message Model

Run ``` python manage.py runserver ```

then go to [127.0.0.1:8000/admin](http://127.0.0.1:8000/admin/). Login with your account you have created step before. Then click the ```Messages```.  Click ```ADD MESSAGE``` in the right. Add some message and go to next step.

7. Query with GraphQL server

go to [127.0.0.1:8000/graphql](http://127.0.0.1:8000/graphql). Then type some thing like this:

+ Query all Message

```
    {
        allMessages {
            edges {
            node {
                id, message
            }
            }
        }
    }
```

+ Query Message container character

In here, I assumed that Query message contain `ll` character.

```
{
  allMessages(message_Icontains: "ll") {
    edges {
      node {
        id, message
      }
    }
  }
}
```

+ Query Message with Id

In here, I assumed that Query message has id `TWVzc2FnZVR5cGU6MQ==`.

```
{
  message(id: "TWVzc2FnZVR5cGU6MQ==") {
    message
}
}
```


